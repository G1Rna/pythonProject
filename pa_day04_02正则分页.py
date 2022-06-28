import requests
import re
import os

#正则表达式
#   限定符 （使用()包括字符串则可以实现字符串限定）
#      ?代表前面的字符出现1次或者0次
#      *匹配0个或多个字符
#      +匹配出现1次以上的字符
#      {a-b}匹配出现a到b次的字符    {b}匹配出现6次的字符    {a,}匹配出现a次以上低字符
#   或运算符
#       (a|b)匹配a或者b字符，字符串
#   字符类
#       [abc]+匹配由[]中存在的字符出现1次或1次以上  [a-zA-Z0-9]+匹配全字符  [^0-9]+ 为匹配此外的字符，匹配0-9以外的非数字（包括换行符）
#   元字符
#       \d+等同于数字字符[0-9]+
#       \w+等同于单词字符[a-zA-Z]+
#       \s+空白符（包含tab和换行符）
#       \D+等同于非数字字符[^0-9]+
#       \W+等同于非单词字符[a-zA-Z]+
#       \S+非空白符（包含tab和换行符）
#       .*包含所有字符（除换行符）
#       ^a 匹配行首的a a$匹配行尾的a
#   匹配机制
#       贪婪匹配（默认） 默认匹配更多字符
#       懒惰匹配.+? 匹配少的字符
#   练习：匹配ip字符串
#       [0-9]{1,3}\.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}/b 无法匹配255以上的数字，需要优化
#       优化后：((25[0-5]|2[0-4]\d|[0-1]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[0-1]?\d\d?)

#   https://regex101.com/正则判断网站


if __name__ == '__main__':
    #headers 请求伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'Cookie': 'UM_distinctid=17f62db2261694-0f3f4013cba22a-f791539-1fa400-17f62db226298b; CNZZDATA30043604=cnzz_eid%3D164882820-1646628380-https%253A%252F%252Fwww.baidu.com%252F%26ntime%3D1646628380; _cnzz_CV30043604=forum%7Cfid-7955747%7C0; guestJs=1655703898; ngacn0comUserInfo=G1Rna%09G1Rna%0939%0939%09%0910%090%094%090%090%09; ngacn0comUserInfoCheck=309bd9d6b757538ba75b0dfb9173cac2; ngacn0comInfoCheckTime=1655704148; ngaPassportUid=63770007; ngaPassportUrlencodedUname=G1Rna; ngaPassportCid=X9885b0gucle6e4sd6gprvar0u5d07eegaqicvq2; lastpath=/read.php?tid=32385752&page=2; lastvisit=1655704531; bbsmisccookies=%7B%22uisetting%22%3A%7B0%3A1%2C1%3A1655969547%7D%2C%22pv_count_for_insad%22%3A%7B0%3A-20%2C1%3A1655744494%7D%2C%22insad_views%22%3A%7B0%3A1%2C1%3A1655744494%7D%7D'
    }

    #自定义请求
    #NGA需要更新cookie信息，如果没有登录账号的话需要更新Cookie来运行
    url = 'https://bbs.nga.cn/read.php?tid=32385752&page=%d'
    #配置通用分页模板
    for pageNum in range(1,4):
        newUrl = format(url%pageNum)
        html_data = requests.get(url = newUrl ,headers = headers).text
        ex = "{aid:'',url:'(.*?)',"

        img_src = re.findall(ex,html_data,re.S)

        if len(img_src) != 0:
            if not os.path.exists('./ngaImage1'):
                os.mkdir('./ngaImage1')
            for src in img_src:
                # print(src)
                src = 'https://img.nga.178.com/attachments/'+src
                imgName = src.split('/')[-1].split('.')[0]
                # print(src1)
                # post发送的数据
                # content返回的是二进制的图片数据
                img_data = requests.get(url = src ,headers = headers).content
                with open('./ngaImage1/'+imgName+'.jpg', 'wb') as fp:
                    fp.write(img_data)
            print('成功。当前页面的图片已经下载到目录下的ngaImage文件夹下')
        else:
            print(html_data)
            print('失败，Cookie失效，或主题页已经消失或没有目标。')

