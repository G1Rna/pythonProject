import scrapy


class PatuSpider(scrapy.Spider):
    name = 'Xpath'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.bilibili.com/video/BV1ha4y1H7sx?p=61&spm_id_from=333.880.my_history.page.click&vd_source=3ac094b7b122e7877d4431891f35c982']

    def parse(self, response):
        # print(str(response.body, encoding="utf-8"))
        content = response.xpath('//div[@id="v_desc"]//span[@class="desc-info-text"]/text()')[0].extract()
        print(content)
