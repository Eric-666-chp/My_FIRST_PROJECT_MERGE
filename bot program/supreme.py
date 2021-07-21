import time
from selenium.webdriver import ActionChains
from selenium import webdriver
import win32con
import win32api
import win32clipboard
import pyautogui as pg
import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
import os


# def open_app(app_dir):
#     os.startfile(app_dir)

produce = "shoes"  # 商品类别选择
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
chromedriver = r"D:\python project\bot program\chromedriver.exe"
driver = webdriver.Chrome(options=options, executable_path= chromedriver)
# configPath = r'--user-data-dir=C:\Users\10026\AppData\Local\Google\Chrome\User Data'
# chromeConfig = webdriver.ChromeOptions()
# chromeConfig.add_argument(configPath)
# driver = webdriver.Chrome(chrome_options=chromeConfig)
driver.get("https://www.supremenewyork.com/shop/all/" + produce)  # 目标网址
driver.implicitly_wait(10)
A = time.strftime ("%H:%M:%S")
while A != '11:00:02':
    A = time.strftime("%H:%M:%S")
driver.refresh()
driver.implicitly_wait(10)
driver.find_element_by_link_text("Supreme®/Nike SB Dunk Low").click()  # 商品名称索检
driver.implicitly_wait(10)
time.sleep(0.5)
driver.find_element_by_name("commit").click()
driver.implicitly_wait(10)
time.sleep(0.5)
driver.close()
# if __name__ == "__main__":
#     app_dir = r'C:\Users\10026\OneDrive\桌面\supreme check out.url'
#     open_app(app_dir)





