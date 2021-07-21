import time
from selenium.webdriver import ActionChains
from selenium import webdriver
import win32con
import win32api
import win32clipboard
import pyautogui as pg

driver = webdriver.Chrome(r'D:\Python newbe\Chromedriver\chromedriver_win32\chromedriver.exe')
driver.get("https://www.nike.com/orders/gift-card-lookup")
time.sleep(2)
f = open('number.txt','r')
d = open('money.txt','w')
tj=23
N = f.read(19)
f.seek(tj)
P = f.read(6)
driver.find_element_by_xpath("//input[@id='giftCardNumber']").send_keys(N)
pg.doubleClick(x=570,y=620)
driver.find_element_by_xpath("//input[@id='giftCardPIN']").send_keys(P)
driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]").click()
time.sleep(2)
pg.doubleClick(x=333,y=402)
pg.click(button= 'right')
win32api.keybd_event(67,0,0,0)
win32api.keybd_event(67,0,win32con.KEYEVENTF_KEYUP,0)

pg.doubleClick(x=333,y=402)
pg.click(button= 'right')
win32api.keybd_event(67,0,0,0)
win32api.keybd_event(67,0,win32con.KEYEVENTF_KEYUP,0)
win32clipboard.OpenClipboard()
Money = win32clipboard.GetClipboardData(win32con.CF_TEXT)
win32clipboard.CloseClipboard()

Money = str(Money)
d.write(N)
d.write('----')
d.write(P)
d.write('  ')
d.write(str(Money))
xj = driver.find_element_by_xpath("//input[@id='giftCardNumber']")
ActionChains(driver).double_click(xj).perform()
tj = tj+31
N = f.read(20)
f.seek(tj)
P = f.read(6)

while P.strip() != '':
    driver.find_element_by_xpath("//input[@id='giftCardNumber']").send_keys(N)
    time.sleep(0.5)
    pg.doubleClick(x=570,y=620)
    driver.find_element_by_xpath("//input[@id='giftCardPIN']").send_keys(P)
    driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]").click()
    time.sleep(2)
    pg.doubleClick(x=333, y=402)
    pg.click(button='right')
    win32api.keybd_event(67,0,0,0)
    win32api.keybd_event(67,0,win32con.KEYEVENTF_KEYUP,0)
    win32clipboard.OpenClipboard()
    Money = win32clipboard.GetClipboardData(win32con.CF_TEXT)

    win32clipboard.CloseClipboard()
    pg.doubleClick(x=333, y=402)
    pg.click(button='right')
    win32api.keybd_event(67, 0, 0, 0)
    win32api.keybd_event(67, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32clipboard.OpenClipboard()
    Money = win32clipboard.GetClipboardData(win32con.CF_TEXT)
    win32clipboard.CloseClipboard()

    Money = str(Money)
    d.write(N)
    d.write('----')
    d.write(P)
    d.write('  ')
    d.write(str(Money))
    ActionChains(driver).double_click(xj).perform()
    tj = tj+31
    N = f.read(20)
    f.seek(tj)
    P = f.read(6)

f.close()
d.close()