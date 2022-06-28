#当前爬虫的页面是樱花动漫，时间：2022年6月13日15:03:45
#因为登录页面存在验证码，目前无法对验证码进行解析，暂时无法获取session



import requests

#请求目标地址
url = 'http://www.dmh8.com/user/upgrade.html'

#登录请求地址
loginUrl='http://www.dmh8.com/user/login.html'

#headers 请求伪装
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Safari/537.36'
}

req = requests.session()

data={
'user_name': '541781026',
'user_pwd': 'lby980809'
}
res=req.post(url=loginUrl,headers = headers,data = data)

code = req.status_code
print(code)

if(code == 200):
    res = req.get(url=url,headers= headers)
    with open('./test.html','wb') as fp:
        fp.write(res.text.encode('utf-8'))
