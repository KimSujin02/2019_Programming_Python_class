import pyautogui as pag     #
import time     #sleep

if __name__ == '__main__':
    pag.moveTo(400, 350, duration=2)
    pag.click()
    pag.typewrite("Happy birthday to me", interval=0.5)
    pag.press("enter")
    pag.typewrite("waba raba dub dub")
    pag.press("enter")
    pag.press("hangul")
    pag.typewrite("tnwlsdk toddlf cnrgkgo!")