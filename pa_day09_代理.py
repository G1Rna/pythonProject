import requests

if __name__ == "__main__":
    url = 'https://whoer.net/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            }
    html = requests.get(url=url, headers=headers,proxies={"https":"45.167.124.5:9992"}) #当前使用的为哥伦比亚节点
    #https://www.freeproxylists.net/zh/  可以查询免费的IP代理  具有时效性，可能明天就没有这个网站了
    #匿名度：透明（服务器知道请求用了代理，并且也知道真实IP），匿名（服务器知道请求用了代理，但是不知道真实IP），高匿名（服务器不知道请求用了代理，也不知道真实IP）
    #2022年6月22日14:53:33 当前非透明的免费ip代理已经近乎没有
    html_text = html.text
    code = html.status_code
    if (code == 200):
        with open('./ip.html', 'wb') as fp:
            fp.write(html_text.encode('utf-8'))
        print("完成！请查看ip.html")
