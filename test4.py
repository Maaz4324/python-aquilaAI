import pyautogui
import time
from pynput.keyboard import Key, Controller

# def newtab():
#     cords = pyautogui.locateCenterOnScreen('newtab.png')
#     pyautogui.click(cords)

def classroomOpen():
    cords = pyautogui.locateCenterOnScreen('openclassroom.png')
    pyautogui.click(cords)

def MathClassroom():
    cords = pyautogui.locateCenterOnScreen('MathClassroom.png')
    pyautogui.click(cords)

def MathClassroomLink():
    cords = pyautogui.locateCenterOnScreen('linkpwd.png')
    pyautogui.click(cords)

def zoomOpen():
    cords = pyautogui.locateCenterOnScreen('openZoomMeetings.png')
    pyautogui.click(cords)

def openChat():
    cords = pyautogui.locateCenterOnScreen('openChat.png')
    pyautogui.click(cords)

def typechat():
    cords = pyautogui.locateCenterOnScreen('typechat.png')
    pyautogui.click(cords)

# classroomOpen()
# time.sleep(10)
# MathClassroom()
# time.sleep(8)
# MathClassroomLink()
# time.sleep(9)
# zoomOpen()
# time.sleep(5)
# openChat()
# time.sleep(2)
# typechat()
keyboard = Controller()
time.sleep(5)
keyboard.type("yes sir")



# def youtube():
#     cords = pyautogui.locateCenterOnScreen('youtube.png')
#     pyautogui.click(cords)

# def minimize():
#     cords = pyautogui.locateCenterOnScreen('minimize.png')
#     pyautogui.click(cords)

# minimize()

# newtab()
# time.sleep(5)

# youtube()





# time.sleep(5)

# keyboard.press('a')
# keyboard.release('a')

# keyboard.press(Key.cmd)
# keyboard.release(Key.cmd)

