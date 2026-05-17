import pyautogui
import os
import time

print("Anti-theft system armed...\n")

last_position = pyautogui.position()

while True:

    current_position = pyautogui.position()

    if current_position != last_position:

        print("Movement detected!")
        print("Locking system...")

        os.system("rundll32.exe user32.dll,LockWorkStation")

        break

    last_position = current_position

    time.sleep(1)