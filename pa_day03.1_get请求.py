import requests

#自定义请求
purl = 'http://www.dmh8.com/'
#headers 请求伪装
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Safari/537.36'
}


res=requests.get(purl,headers = headers)

code = res.status_code

print(code)
if(code == 200):
    with open('./test.html','wb') as fp:
        fp.write(res.text.encode('utf-8'))
