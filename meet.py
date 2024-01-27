import pyautogui
import time


pyautogui.press('win', interval = 0.5)
time.sleep(1)
pyautogui.write("computer",interval=0.5)
pyautogui.press('Enter',interval=0.5)
pyautogui.write("LOCAL DISK D")
pyautogui.press('Enter',interval=0.5)
pyautogui.write("LOCAL DISK D")
time.sleep(1)
pyautogui.write("LOCAL DISK")
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(x=304,y=307)
pyautogui.press('enter')
pyautogui.click(x=402,y=121)
pyautogui.press('enter')