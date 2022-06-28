from selenium import webdriver
from lxml import etree
import time
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")

    input = driver.find_element_by_id('kw')
    buttom = driver.find_element_by_id('su')
    input.send_keys('百度翻译')
    buttom.click()
    # driver.execute_script('')#执行js代码
    # driver.forward()#前进
    # driver.back()#后退
    time.sleep(10)

    driver.quit()

