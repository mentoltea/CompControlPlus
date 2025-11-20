import os, sys
import subprocess
import time

time.sleep(50)
# subprocess.Popen(["python3", "main.py"])
process = subprocess.Popen([sys.executable, 'main.py'])
# os.system("python3 reboot.py")
# import main