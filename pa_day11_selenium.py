from selenium import webdriver
from lxml import etree
import time
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.bilibili.com/")
    page_text = driver.page_source

    tree = etree.HTML(page_text)
    titles = tree.xpath('//div[@class="recommend-container__2-line"]/div[@class="bili-video-card is-rcmd"]//h3[@class="bili-video-card__info--tit"]')
    # print(titles)

    for title in titles:
        name = title.xpath('./@title')
        print(name)
    time.sleep(35)
    driver.quit()

