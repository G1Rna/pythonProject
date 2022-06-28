from multiprocessing import Pool
import requests
import re
import os
#headers中的referer很重要，关系到是否能下载成功
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'Referer': 'https://www.bilibili.com/'
}
#可以减少requests.get代码量
def get_url(url):
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    res.encoding = res.apparent_encoding
    return res
def getCid(Bid):
    cidUrl = 'https://api.bilibili.com/x/player/pagelist?bvid=' + Bid + '&jsonp=jsonp'#可以通过页面F12筛选得到url
    cid = get_url(url=cidUrl).json()['data'][0]['cid']
    return str(cid)
#自己写的正则取出Aid
def getAid(Bid):
    pageUrl = 'https://www.bilibili.com/video/' + Bid
    pageHtml= get_url(pageUrl).text
    ex = "{\"aid\":(.*?),\"bvid\":"
    aid = re.findall(ex, pageHtml, re.S).pop(-1)
    return aid
#大佬的Aid算法
def BV_to_AV(bv):
    # 方法：BV1j4411W7F7
    if bv.isdigit():
        return bv
    bv = list(bv[2:])
    keys = {'1': 13, '2': 12, '3': 46, '4': 31, '5': 43, '6': 18, '7': 40, '8': 28, '9': 5,
            'A': 54, 'B': 20, 'C': 15, 'D': 8, 'E': 39, 'F': 57, 'G': 45, 'H': 36, 'J': 38, 'K': 51, 'L': 42, 'M': 49,
            'N': 52, 'P': 53, 'Q': 7, 'R': 4, 'S': 9, 'T': 50, 'U': 10, 'V': 44, 'W': 34, 'X': 6, 'Y': 25, 'Z': 1,
            'a': 26, 'b': 29, 'c': 56, 'd': 3, 'e': 24, 'f': 0, 'g': 47, 'h': 27, 'i': 22, 'j': 41, 'k': 16, 'm': 11,
            'n': 37, 'o': 2, 'p': 35, 'q': 21, 'r': 17, 's': 33, 't': 30, 'u': 48, 'v': 23, 'w': 55, 'x': 32, 'y': 14,
            'z': 19}
    for i in range(len(bv)):
        bv[i] = keys[bv[i]]
    bv[0] *= (58 ** 6)
    bv[1] *= (58 ** 2)
    bv[2] *= (58 ** 4)
    bv[3] *= (58 ** 8)
    bv[4] *= (58 ** 5)
    bv[5] *= (58 ** 9)
    bv[6] *= (58 ** 3)
    bv[7] *= (58 ** 7)
    bv[8] *= 58
    return str((sum(bv) - 100618342136696320) ^ 177451812)
def getTitle(Bid):
    infoUrl = 'https://api.bilibili.com/x/web-interface/view?aid='+getAid(Bid)+'&cid='+getCid(Bid)
    infoRes = get_url(infoUrl).json()
    # 没想好这部分怎么用
    title = infoRes['data']['title']
    return title
def downLoad(dic):
    print('开始下载：'+str(dic['title']))
    url = 'https://api.bilibili.com/x/player/playurl?cid=' + getCid(dic['Bid']) + '&bvid=' + dic['Bid'] + '&qn=64'  # 注：此处url目前不知道怎么获取，目前为查阅别人的爬虫文章得知
    # url = 'https://api.bilibili.com/x/player/playurl?avid='+BV_to_AV(Bid)+'&cid=' + getCid(Bid) + '&qn=64'  # 注：此处url目前不知道怎么获取，目前为查阅别人的爬虫文章得知 目前没有方法直接得知aid，不过有算法
    videoUrl = get_url(url).json()['data']['durl'][0]['url']
    videoData = get_url(videoUrl).content
    print(str(dic['title'])+'下载中......')
    if not os.path.exists('./B站视频'):
        os.mkdir('./B站视频')
    # with open(r'./B站视频/' + dic['title'] + '.flv', 'wb') as fp:
    with open('./B站视频/' + dic['title'] + '.flv', 'wb') as fp:
        fp.write(videoData)
    print(str('下载完成：'+dic['title']))
def createDic(Bids):
    dicLst = []
    for bid in Bids:
        dic = {}
        dic['Bid'] = bid
        title = re.findall(r'[^*"/:?\|<>]', getTitle(bid), re.S)
        dic['title'] = "".join(title)
        dicLst.append(dic)
    return dicLst
if __name__ == '__main__':
    Bids = {'BV1Si4y1t7bP','BV163411B71r','BV1rE411J7Qf','BV1254y1f7Ne'}
    pool = Pool(5)
    pool.map(downLoad,createDic(Bids))
    pool.close()
    pool.join()





