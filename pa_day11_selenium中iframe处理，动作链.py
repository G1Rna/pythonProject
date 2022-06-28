from selenium import webdriver
from lxml import etree
import time
#导入动作链
from selenium.webdriver import ActionChains
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")

    driver.switch_to_frame('text')#切换浏览器标签定位的作用域
    div = driver.find_element_by_id('text')
    action = ActionChains(driver)
    action.click_and_hold(div)
    for i in range(5):
        action.move_by_offset(0,12).perform()#move_by_offset(x,y)
        # action.perform()
    action.release()#释放动作
    time.sleep(10)

    driver.quit()

