import time
import random
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

x = 0
Num_for_account = 111780

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')l
# options.add_argument('--disable-gpu')
# options.add_argument('--no-sandbox')
# chromedriver = r"D:\python project\Nike auto make account\chromedriver.exe"
# driver = webdriver.Chrome(options=options, executable_path= chromedriver)
while x < 100:
    Gmail_account = 'er' + str(Num_for_account)
    driver = webdriver.Chrome()
    driver.get('https://www.nike.com/login')
    driver.implicitly_wait(20)
    time.sleep(1)
    driver.find_element_by_link_text("Join Us.").click()
    driver.implicitly_wait(20)
    time.sleep(1)
    driver.find_element_by_name("emailAddress").click()
    driver.implicitly_wait(10)
    pg.write(Gmail_account + "@gmail.com", interval=0.2)
    driver.find_element_by_name("password").click()
    driver.implicitly_wait(10)
    pg.write("Meiling520", interval=0.2)
    driver.find_element_by_name("firstName").click()
    driver.implicitly_wait(10)
    pg.write("Eric", interval=0.2)
    driver.find_element_by_name("lastName").click()
    driver.implicitly_wait(10)
    pg.write("Chen", interval=0.2)
    driver.find_element_by_name("dateOfBirth").click()
    driver.implicitly_wait(10)
    pg.write("2000000506", interval=0.2)
    driver.find_element_by_xpath("//span[contains(text(),'Male')]").click()
    driver.implicitly_wait(10)
    driver.find_element_by_name("dateOfBirth").click()
    pg.write("2000", interval=0.2)
    time.sleep(1)
    driver.find_element_by_name("emailAddress").click()
    pg.press("enter")
    time.sleep(1)
    driver.close()
    f = open("Nike account.txt","a")
    f.write(Gmail_account + "@gmail.com" + "  Month: 5" + '\n')
    f.close()
    x = x+1
    a = str(x)
    print(Num_for_account)
    print("\ntotal make " + a + " accounts")
    Num_for_account = Num_for_account + 2
    time.sleep(120)
    print("wait for 10 min")
    time.sleep(120)
    print("wait for 8 min")
    time.sleep(120)
    print("wait for 6 min")
    time.sleep(120)
    print("wait for 4 min")
    time.sleep(120)
    print("wait for 2 min")