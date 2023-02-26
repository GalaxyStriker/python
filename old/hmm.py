import pyautogui
import time
import random

for _ in range(10):
    x = random.randint(300,700)
    y = random.randint(600,900)
    pyautogui.moveTo(x,y,0.3)
    time.sleep(3)