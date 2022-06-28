from bs4 import BeautifulSoup
import requests
import re
import os

if __name__ == "__main__":

    # 自定义请求
    url = 'http://www.dmh8.com/'#樱花动漫  经常换域名，如果报错需要更新
    # headers 请求伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Safari/537.36'
    }

    # 实例化网站soup对象
    html_text = requests.get(url, headers=headers).text
    soup1= BeautifulSoup(html_text, 'lxml')

    imgHtml = soup1.select('.myui-vodlist__thumb')

    if not os.path.exists('./樱花动漫首页图片'):
        os.mkdir('./樱花动漫首页图片')
    for i in range(0,len(imgHtml)):
        #['href'] 获取指定的内容
        # print(imgSrc[i]['data-original'])
        ex = "(.*?).jpg"
        img_src = re.findall(ex,imgHtml[i]['data-original'],re.S)
        img_name = imgHtml[i]['title']
        if len(img_src) !=0:
            for src in img_src:
                src = src+'.jpg'
                img_data = requests.get(url=src,headers=headers).content
                with open('./樱花动漫首页图片/'+img_name+'.jpg','wb') as fp:
                    fp.write(img_data)
    print('成功。首页图片已经下载到‘樱花动漫首页图片’文件夹下')