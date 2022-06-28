import requests
import time

from PIL import Image
from selenium import webdriver
from chaojiying import Chaojiying_Client
def part_screenshot(driver):
    driver.save_screenshot("hello1.png")
    return Image.open("hello1.png")

def get_image(driver):  # 对验证码所在位置进行定位，然后截取验证码图片
    img = driver.find_element_by_xpath('//*[@id="verify_img"]')
    time.sleep(2)
    location = img.location
    print(location, 111)
    size = img.size
    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']
    page_snap_obj = part_screenshot(driver)
    image_obj = page_snap_obj.crop((left, top, right, bottom))
    return image_obj  # 得到的就是验证码

if __name__ == '__main__':


    driver = webdriver.Chrome()
    driver.get("http://www.dmh8.com/user/login.html")
    print(driver.title)  # 打印页面的标题
    b = get_image(driver)
    b.save("1.png")

    chaojiying = Chaojiying_Client('541781026', 'lby980809', '935325')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('./1.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    # {'err_no': 0, 'err_str': 'OK', 'pic_id': '1181316400902150004', 'pic_str': '7261', 'md5': '61fa9ced45eb272e98849687c58a2c68'}
    verify_num = chaojiying.PostPic(im, 1902)['pic_str']

    user_input = driver.find_element_by_id('user_name')
    pwd_input = driver.find_element_by_id('user_pwd')
    verify_input = driver.find_element_by_id('verify')
    login_buttom = driver.find_element_by_id('btn_submit')

    user_input.send_keys('541781026')
    time.sleep(2)
    pwd_input.send_keys('lby980809')
    time.sleep(2)
    verify_input.send_keys(verify_num)
    time.sleep(2)
    login_buttom.click()
    time.sleep(15)


    driver.quit()  # 一定要退出！不退出会有残留进程！

# loginUrl='http://www.dmh8.com/user/login.html'
#
# res=requests.get(url=loginUrl)
#
# code = res.status_code
#
# print(code)
# if(code == 200):
#     with open('./test.html','wb') as fp:
#         fp.write(res.text.encode('utf-8'))

