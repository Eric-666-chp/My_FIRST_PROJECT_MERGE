from selenium import webdriver
import time


# 模块功能：‘打开网页、输入数据、返回结果’
# def Open_Webpage():
#     with open('number.txt', 'r') as f:
#         tj = 23
#         N = f.read(19)
#         f.seek(tj)
#         P = f.read(6)
#         driver = webdriver.Chrome()
#         driver.get('https://www.nike.com/orders/gift-card-lookup')
#         time.sleep(2)
#         driver.find_element_by_xpath("//input[@id='giftCardNumber']").send_keys(N)
#         driver.find_element_by_xpath("//input[@id='giftCardPIN']").send_keys(P)
#         driver.find_element_by_xpath(
#             "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/button[1]").click()


# 模块功能：‘读取账号和密码'
def Get_Number():
    tj = 0
    with open('number.txt', 'r') as f:
        tj = tj + 23
        N = f.read(19)
        f.seek(tj)
        P = f.read(6)
        print(P, N)




# 模块功能：’保存账号剩余钱数’
# def Download_data(data):
#     with open('money.txt', 'w') as d:
#         while data[0].strip() != '':
#             d.write(data[1])
#             d.write('----')
#             d.write(data[0])
#             d.write('  $')


data = Get_Number()
print(data)
