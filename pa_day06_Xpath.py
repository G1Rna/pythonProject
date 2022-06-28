import requests
from lxml import etree

if __name__ == "__main__":
    parser = etree.HTMLParser(encoding="utf-8")
    selector = etree.parse('./test.html', parser=parser)
    # r = selector.xpath('/html/head/title')

    # r = selector.xpath('//title')  #//表示多个层级
    # [@class]  @后面跟选择器
    # r = selector.xpath('//ul[@class="myui-vodlist__text col-pd clearfix col-lg-wide-33 col-md-wide-33"]')
    # r = selector.xpath('//ul[@id="test1"]')

    # title = selector.xpath('//ul[@id="test1"]/li[1]')#[1]索引定位，可以定位任意标签 start:1
    # title = selector.xpath('//ul[@id="test1"]/li[2]/a/text()')  #/text()获取标签直系内容  //text()获取便签下所有内容
    title  = selector.xpath('//ul[@id="test1"]/li[2]/a//text()')[-1]
    episode = selector.xpath('//ul[@id="test1"]/li[2]/a//text()')[1]
    href = selector.xpath('//ul[@id="test1"]/li[2]/a/@href')[0] #@href取属性
    url = "http://www.dmh8.com"+href
    print("《"+title.strip()+"》"+episode+",播放地址："+url)
