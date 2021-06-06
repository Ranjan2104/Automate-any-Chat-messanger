# Amresh Ranjan.

import pyautogui
import time

time.sleep(5)

text = 'I Love Python'

while True:
    pyautogui.typewrite(text)
    
    time.sleep(1)
    pyautogui.press('enter')


