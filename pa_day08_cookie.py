import requests


if __name__ == "__main__":
    url = 'http://www.dmh8.com/user/index.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'cookie':'PHPSESSID=0trvo2g3n84828hbuld781mef2; Hm_lvt_ea6972a9380e5a8a6607cc4c62409955=1655360604,1655707053,1655791592,1655862037; user_id=17684; user_name=541781026; group_id=2; group_name=%E9%BB%98%E8%AE%A4%E4%BC%9A%E5%91%98; user_check=66ef1f768c6d48e57a4dc6664d11917a; user_portrait=%2Fstatic%2Fimages%2Ftouxiang.png; Hm_lpvt_ea6972a9380e5a8a6607cc4c62409955=1655863191'
    }
    htmlText = requests.get(url, headers=headers).text
    with open('./user.html', 'wb') as fp:
        fp.write(htmlText.encode('utf-8'))
    print("完成！请查看user.html")