from selenium import webdriver
import os
import json


def browser_initial():
    """"
    浏览器初始化,并打开大麦网购票界面（未登录状态）
    """
    browser = webdriver.Chrome()
    browser.get('https://www.supremenewyork.com/shop/all')
    return browser


def log_damai(browser):
    """
    从本地读取cookies并刷新页面,成为已登录状态
    """
    with open('damai_cookies.txt', 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())

    # 往browser里添加cookies
    for cookie in listCookies:
        cookie_dict = {
            'domain': '.damai.cn',
            'name': cookie.get('name'),
            'value': cookie.get('value'),
            "expires": '',
            'path': '/',
            'httpOnly': False,
            'HostOnly': False,
            'Secure': False
        }
        browser.add_cookie(cookie_dict)
    browser.refresh()  # 刷新网页,cookies才成功


if __name__ == "__main__":
    browser = browser_initial()
    log_damai(browser)
