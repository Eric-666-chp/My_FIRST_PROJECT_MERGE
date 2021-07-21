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

name = "Eric Chen"
email = "1002685117eric@gmail.com"
tel = "9294027036"
address = "41-05 College Point Blvd"
apt = "Apt 2E"
zipcode = "11355"
number = "5524332648928300"
month = "11"
year = "2024"
cvv = "593"
produce = "accessories"  # 商品类别选择
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
chromedriver = r"D:\python project\bot program\chromedriver.exe"
driver = webdriver.Chrome(options=options, executable_path= chromedriver)
configPath = r'--user-data-dir=C:\Users\10026\AppData\Local\Google\Chrome\User Data'
chromeConfig = webdriver.ChromeOptions()
chromeConfig.add_argument(configPath)
driver = webdriver.Chrome(chrome_options=chromeConfig)
driver.get("https://www.supremenewyork.com/shop/all/"+ produce)  # 目标网址
driver.implicitly_wait(10)
driver.find_element_by_link_text("Supreme®/Hanes® Crew Socks (4 Pack)").click()  # 商品名称索检
driver.implicitly_wait(10)
driver.find_element_by_name("commit").click()
driver.implicitly_wait(10)