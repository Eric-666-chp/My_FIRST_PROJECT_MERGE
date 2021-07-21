from selenium.webdriver import ActionChains
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
chromedriver = r"D:\python project\bot program\chromedriver.exe"
driver = webdriver.Chrome(options=options, executable_path= chromedriver)
driver.get("https://www.supremenewyork.com/shop/all")
driver.save_screenshot("tupian.png")
driver.close()
