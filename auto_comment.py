import pyautogui
import time

comments = ["cat ", "rabbit ", "donkey", "dear", "elephant"]


for n in comments:
    me = "I like " + n

    pyautogui.typewrite(me)
    pyautogui.typewrite("\n")
    time.sleep(1)
