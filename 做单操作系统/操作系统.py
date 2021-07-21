import pyautogui as pg
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# configPath = r'--user-data-dir=C:\Users\10026\AppData\Local\Google\Chrome\User Data'
# chromeConfig = webdriver.ChromeOptions()
# chromeConfig.add_argument(configPath)
# driver = webdriver.Chrome(options=chromeConfig)
# driver.get("https://docs.google.com/spreadsheets/d/1TBjI80Rc9Pm9BHnyaEvVenwpsRFPZ269DVGRKWtJJJs/edit#gid=0")
# driver.implicitly_wait(10)
# time.sleep(1)
# pg.press('enter')
# time.sleep(1)
# pg.press('enter')
# pg.press('enter')
# time.sleep(1)
# driver.find_element_by_xpath("/html[1]/body[1]/div[6]/div[1]/div[2]/div[1]/div[5]/div[2]/div[1]/div[2]").send_keys("WWW")
# pg.write(Item_No)
# pg.press('tab')
# pg.write(shoe_name)
# pg.press('tab')
# pg.write(shoe_size)
# pg.press('tab')
# pg.write(sales_platform)
# pg.press('tab')
# pg.write(purchase_price)
# pg.press('tab')
# pg.write(sell_price)
# pg.press('enter')

status = 'go'
while True:
    shoe_size = []
    shoes_number = []
    Item_No= input("货号：")
    shoe_name = input("鞋子名称：")
    while True:
        size = input("鞋码：")
        if size == '0':
            break
        shoe_size.append(size)
    num = len(shoe_size)
    num2 = num
    i = 0
    while num > 0:
        number = input(shoe_size[i] + "鞋码数量：")
        shoes_number.append(number)
        i = i + 1
        num = num - 1
    sales_platform = input("销售平台：")
    purchase_price = input("进货价格：")
    sell_price = input("卖出价格：")
    time.sleep(4)
    while num < num2:
        pg.write(Item_No)
        pg.press('tab')
        pg.write(shoe_name)
        pg.press('tab')
        pg.write(shoe_size[num])
        pg.press('tab')
        pg.press(shoes_number[num])
        pg.press('tab')
        pg.write(sales_platform)
        pg.press('tab')
        pg.write("$" + purchase_price)
        pg.press('tab')
        pg.write("$" + sell_price)
        pg.press('enter')
        # print(Item_No + " " + shoe_name + " " + shoe_size[num] + " " + shoes_number[num] + " " + sales_platform + " " + "$" + purchase_price + " " + "$" + sell_price + " ")
        num = num + 1
