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
from selenium.webdriver.common.keys import Keys

x = 0
Num_for_account = 111656
# A = time.strftime("%H:%M:%S")
# options = webdriver.ChromeOptions()


# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# options.add_argument('--no-sandbox')
# chromedriver = r"D:\python project\bot program\chromedriver.exe"
# driver = webdriver.Chrome(options=options, executable_path= chromedriver)
# A = time.strftime("%H:%M:%S")
# while A < '00:11:00':
#     A = time.strftime("%H:%M:%S")
while x < 100:
    Gmail_account = 'er' + str(Num_for_account)
    driver = webdriver.Chrome()
    driver.get('https://www.nike.com/login')
    driver.implicitly_wait(10)
    time.sleep(1)
    driver.find_element_by_link_text("Join Us.").click()
    driver.implicitly_wait(10)
    time.sleep(1)
    driver.find_element_by_name("emailAddress").send_keys(Gmail_account + "@gmail.com")
    driver.implicitly_wait(10)
    time.sleep(0.5)
    driver.find_element_by_name("password").send_keys("Meiling520")
    driver.implicitly_wait(10)
    time.sleep(0.7)
    driver.find_element_by_name("firstName").send_keys("Eric")
    driver.implicitly_wait(10)
    time.sleep(1.5)
    driver.find_element_by_name("lastName").send_keys('Chen')
    driver.implicitly_wait(10)
    time.sleep(0.5)
    driver.find_element_by_name("dateOfBirth").send_keys("2000000902")
    driver.implicitly_wait(10)
    time.sleep(1)
    driver.find_element_by_xpath("//span[contains(text(),'Male')]").click()
    driver.implicitly_wait(10)
    time.sleep(0.7)
    driver.find_element_by_name("dateOfBirth").send_keys("2000")
    time.sleep(0.8)
    driver.find_element_by_name("emailAddress").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.close()
    f = open("Nike account.txt", "a")
    f.write(Gmail_account + "@gmail.com" + "  Month: 9" + '\n')
    f.close()
    x = x + 1
    a = str(x)
    print(Num_for_account)
    print("\ntotal make " + a + " accounts")
    Num_for_account = Num_for_account + 1
    time.sleep(120)
    print("wait for 11 min")
    time.sleep(120)
    print("wait for 9 min")
    time.sleep(120)
    print("wait for 7 min")
    time.sleep(120)
    print("wait for 5 min")
    time.sleep(120)
    print("wait for 3 min")
    time.sleep(120)
    print("wait for 1 min")
    time.sleep(60)
