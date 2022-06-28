import requests


if __name__ == '__main__':
    #自定义请求
    url = ''

    #headers 请求伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    }

    #post发送的数据
    #content返回的是二进制的图片数据
    img_data = requests.post(url = url ,headers = headers).content

    with open('./img.jpg','wb') as fp:
        fp.write(img_data)
