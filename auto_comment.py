from turtle import hideturtle
import pyautogui
import time

#comments = ["model 1 size 43 @chakriya_met @twilight_anonymous @_han_nahhh_"]
comments =["hi"]
# time.sleep(5)
# pyautogui.typewrite(comments[0])
# pyautogui.typewrite("\n")
# time.sleep(1)

i = 0


while i < 100:


    pyautogui.typewrite(comments[0])
    pyautogui.typewrite("\n")
    time.sleep(0.5)


    i = i + 1
