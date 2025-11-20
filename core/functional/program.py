import subprocess
import os, sys
import deinit

def reboot():
    deinit.deinitialize()
    # subprocess.Popen(['python3', 'reboot.py'])
    process = subprocess.Popen([sys.executable, 'reboot.py'])
    # os.system("& .venv/Scripts/activate.bat")
    # os.system("python3.exe reboot.py")
    # import reboot
    exit(0)