from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":

    # 自定义请求
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    # headers 请求伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Safari/537.36'
    }

    # 实例化网站soup对象
    html_content = requests.get(url, headers=headers).content
    soup= BeautifulSoup(html_content, 'lxml')

    li_html = soup.select('.book-mulu > ul > li')
    fp = open('./三国演义/content.txt','w',encoding='utf-8')
    for li in li_html:
        title = li.a.string
        href = 'https://www.shicimingju.com'+li.a['href']
        page_html_content = requests.get(href, headers=headers).content
        soup1 = BeautifulSoup(page_html_content, 'lxml')
        content = soup1.find('div', class_='chapter_content').text
        fp.write(title + ":" + content + "\n")
        print(title + "已爬取")



