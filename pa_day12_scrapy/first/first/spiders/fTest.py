import scrapy


class FtestSpider(scrapy.Spider):
    #爬虫文件名称：爬虫文件的唯一标识
    name = 'fTest'
    #允许的域名（建议不使用）
    # allowed_domains = ['www.baidu.com']
    #起始的url列表
    start_urls = ['https://www.baidu.com/','https://www.bilibili.com/']

    #用于数据解析， response参数表示的就是请求成功后对应的响应对象
    def parse(self, response):

        print(response)
