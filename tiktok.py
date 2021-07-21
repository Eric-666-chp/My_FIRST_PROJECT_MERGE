import pyautogui as pg
import time
import pyautogui
import pyperclip

time.sleep(2)
f = open('pp.txt','r',encoding='utf-8')
tj=5
P = f.read(5)
i = 0
while P.strip() != '':
    time.sleep(0.5)
    P = P.strip('\n')
    pyperclip.copy("芊芊你真的是"+P)
    pyautogui.hotkey('ctrl', 'v')
    pg.click(x=1584, y=1301)
    time.sleep(0.01)
    pg.click(x=1584, y=1301)
    time.sleep(0.01)
    pg.click(x=777, y=1060)
    time.sleep(0.01)
    pg.click(x=1083, y=1310)
    P = f.read(5)
    tj = tj + 5