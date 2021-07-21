import time
from selenium.webdriver import ActionChains
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import win32con
import win32api
import win32clipboard
import pyautogui, sys
print("Press Ctrl-C to quit")
try:
    while True:
        x,y = pyautogui.position()
        positionStr= 'X: ' + str(x).rjust(4) + ' Y: ' +str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr),end='', flush=True)
except KeyboardInterrupt:
    print('\n')

