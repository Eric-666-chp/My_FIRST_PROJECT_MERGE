# Program ID: Wechat auto respond
# Author: Eric Chen
# Purpose: Wechat auto respond

# 头文件导入
import pyautogui as pg
import time
import pyautogui
import pyperclip

# 给予用户2秒等待时间
time.sleep(2)

# 打开存有要说的话的文件夹 文件名为'pp.txt'
f = open('pp.txt','r',encoding='utf-8')

# 设置文件读取字数
tj=5
P = f.read(5)
i = 0

# 循环输出文件内容
while P.strip() != '':
    time.sleep(0.5)
    P = P.strip('\n')
    pyperclip.copy("王小姐你真的是"+P)  # 在(" ")中输入人名,然后+文件内容
    pyautogui.hotkey('ctrl', 'v')
    pg.press("enter")
    P = f.read(5)
    tj = tj + 5











































































































































