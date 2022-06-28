from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":

    # 自定义请求
    purl = 'http://www.dmh8.com/'
    # headers 请求伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Safari/537.36'
    }

    # 实例化本地soup对象
    fp = open('./test.html','r',encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')

    # 实例化网站soup对象
    html_text = requests.get(purl, headers=headers).text
    soup1= BeautifulSoup(html_text, 'lxml')

    #输出测试
    # print(soup)
    # print('--------------------------------------------------------------------------------------------------------')
    # print(soup1)

    # 返回html中第一次出现的tagName
    # print(soup1.img) soup.tagName

    ##.find()
    # 同soup.tagName
    # soup1.find('a') soup.find(tagName)
    #  soup.find(tagName,class_)  class_为类名 class_必须带下划线_
    # print(soup1.find('a',class_='myui-vodlist__thumb lazyload'))
    ##.find_all()
    #同find 只是返回了所有的标签 返回list
    # print(soup.find_all('a',class_='myui-vodlist__thumb'))

    ##.select()
    #select 可以使用类选择器（.），id选择器（#）,标签选择器 >(表示一个层级)  '空格'表示多个层级 span,层级选择器[]
    #返回list
    # print(soup1.select('.myui-vodlist__thumb'))

    #获取标签之间的文本数据 .text/.get_text()/.string
    #.text/.get_text()可以获取所有的文本内容
    # print(soup1.select('.myui-vodlist__thumb')[0].text)
    # print(soup1.select('.myui-vodlist__thumb')[0].get_text())
    #.string只能获取该标签下面的直系文本内容
    # print(soup1.select('.myui-vodlist__thumb')[0].string)

    #['href'] 获取指定的内容
    # print(soup1.select('.myui-vodlist__thumb')[0]['data-original'])

