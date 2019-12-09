import pyautogui as pag
import time     #sleepell

if __name__ == '__main__':
    #메모장 프로그램 실행하자
    pag.click(88, 1055, duration=1)
    pag.click(154, 994, duration=0.5)

    pag.typewrite("memo", interval=0.5)
    pag.press("enter")

    time.sleep(2)

    pag.click(233, 322, duration=1)
    #헬로월드 치자
    pag.typewrite("Hello world", interval=0.1)
    #두번 내리자
    pag.press("enter")
    pag.press("enter")
    #반갑다 세상아 치자
    pag.press("hangul")
    pag.typewrite("qksrkqek tptkddk", interval=0.1)
    #저장하자
    # pag.keyDown('ctrl')
    # pag.press("s")
    # pag.keyUp('ctrl')
    pag.hotkey('ctrl', 's')
    time.sleep(1)
    #파일이름 : 파이썬 월드
    pag.press("hangul")
    pag.typewrite("C:\\Users\\User\\Downloads\\")
    pag.press("hangul")
    pag.typewrite("vkdlTjs dnjfem", interval=0.1)
    pag.press("enter")