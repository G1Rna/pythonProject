import requests
from lxml import etree
from chaojiying import Chaojiying_Client

if __name__ == "__main__":

    ######樱花动漫这里登录特殊性，需要用session来登录get验证码再post，使用session会自动保存cookie

    req = requests.session()    #创建session对象

    login_url = 'http://www.dmh8.com/user/login.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            }
    htmlText = req.get(login_url,headers = headers).text

    selector = etree.HTML(htmlText)
    verify_src ='http://www.dmh8.com' + selector.xpath('//img[@id="verify_img"]/@src')[0]
    respones = req.get(url=verify_src, headers=headers)
    verify_data = respones.content
    with open('./验证码/verify_yh.jpg', 'wb') as fp:
        fp.write(verify_data)

    chaojiying = Chaojiying_Client('541781026', 'lby980809', '935325')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('./验证码/verify_yh.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    #{'err_no': 0, 'err_str': 'OK', 'pic_id': '1181316400902150004', 'pic_str': '7261', 'md5': '61fa9ced45eb272e98849687c58a2c68'}
    verify_num = chaojiying.PostPic(im, 1902)['pic_str']
    print('验证码:'+verify_num)

    data = {
        'user_name': '541781026',
        'user_pwd': 'lby980809',
        'verify':verify_num
    }


    res_login = req.post(url=login_url, headers=headers, data=data)
    res_login_html = res_login.text
    ##樱花动漫返回一个json 并不是直接返回html，所以需要通过设置cookie来实现直接登录
    print(res_login_html)
    code = res_login.status_code
    print(code)

    user_url = 'http://www.dmh8.com/user/index.html'
    user_html = req.post(url=user_url, headers=headers)
    user_html_code = user_html.text
    code = user_html.status_code
    if (code == 200):
        with open('./user.html', 'wb') as fp:
            fp.write(user_html_code.encode('utf-8'))
        print("完成！请查看user.html")
