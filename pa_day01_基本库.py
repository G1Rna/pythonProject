import requests

#url
# url = "https://www.baidu.com"
url = "http://localhost:8080/index"

#发起请求
res = requests.get(url)

#获取相应
print(res)
print(res.content)
print(res.content.decode("utf-8"))
print(res.text)
print(res.headers)
print(res.status_code)
print(res.url)
print(res.request.headers)