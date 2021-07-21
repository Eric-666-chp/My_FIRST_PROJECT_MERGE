from selenium import webdriver

name = "Eric Chen"
email = "1002685117eric@gmail.com"
tel = "9294027036"
address = "41-05 College Point Blvd"
apt = "Apt 2E"
zipcode = "11355"
number = "5524332648928399"
month = "11"
year = "2024"
cvv = "598"

driver = webdriver.Firefox()
driver.get("https://www.supremenewyork.com/shop/all")   # 目标网址
driver.implicitly_wait(10)

driver.find_element_by_link_text("accessories").click()     # 商品类别选择
driver.implicitly_wait(10)
driver.find_element_by_link_text("Supreme®/Hanes® Boxer Briefs (4 Pack)").click()   # 商品名称索检
driver.implicitly_wait(10)
driver.find_element_by_name("commit").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//a[contains(@class,'button checkout')]").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath("//input[@id='order_billing_name']").send_keys(name)
driver.implicitly_wait(10)
driver.find_element_by_xpath("//input[@id='order_email']").send_keys(email)
driver.implicitly_wait(10)
driver.find_element_by_xpath("//input[@id='order_tel']").send_keys(tel)
driver.implicitly_wait(10)
driver.find_element_by_xpath("//input[@id='bo']").send_keys(address)
driver.implicitly_wait(10)
driver.find_element_by_xpath("//input[@id='oba3']").send_keys(apt)
driver.implicitly_wait(10)
driver.find_element_by_xpath("//input[@id='order_billing_zip']").send_keys(zipcode)
driver.implicitly_wait(10)
driver.find_element_by_xpath("//input[@id='rnsnckrn']").send_keys(number)
driver.implicitly_wait(10)
driver.find_element_by_xpath("//select[@id='credit_card_month']").send_keys(month)
driver.implicitly_wait(10)
driver.find_element_by_xpath("//select[@id='credit_card_year']").send_keys(year)
driver.implicitly_wait(10)
driver.find_element_by_xpath("//input[@id='orcer']").send_keys(cvv)
driver.implicitly_wait(10)
driver.find_element_by_xpath("//label[@class='has-checkbox terms']//ins[@class='iCheck-helper']").click()
driver.implicitly_wait(10)