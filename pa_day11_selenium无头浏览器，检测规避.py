import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions

if __name__ == '__main__':
    # 无头浏览器设置项，实现无可视化界面操作
    chrome_option = Options()
    chrome_option.add_argument('--headless')
    chrome_option.add_argument('--disable-gpu')

    #规避检测
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])

    driver = webdriver.Chrome(chrome_options=chrome_option,options=option)#设置无头浏览器
    driver.get("https://www.12306.cn/index/")
    print(driver.page_source)
