import requests

#url
# url = "https://www.baidu.com"
# url = "https://www.lmonkey.com"
# url = 'https://r6.tracker.network/'
url = "https://www.douban.com/"
############
#headers 请求伪装
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
#发起请求
res = requests.get(url,headers = headers)
code = res.status_code
print("相应码："+str(code))

if(code == 200):
    with open('./test.html','wb') as fp:
        fp.write(res.text.encode('utf-8'))