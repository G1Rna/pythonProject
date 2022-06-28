import requests

#自定义请求
# purl = 'https://fanyi.baidu.com/sug'
# purl = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'

#headers 请求伪装
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}

word=input('请输入需要翻译的单词：')

#post发送的数据
data = {'query':word}

res=requests.post(url = purl ,headers = headers,data = data)

code = res.status_code
if code == 200:
    print('请求成功')
    data = res.json()
    print(data)
    if data['errno'] == 0:
        print('响应成功')
        k=data['data'][0]['k']
        v = data['data'][0]['v'].split(';')[0]
        print(k)
        print(v)

        print(data['data'][0]['v'].split(';'))