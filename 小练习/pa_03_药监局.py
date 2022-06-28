#网站更新，目前无法通过Xpath爬取JSON数据


# url = 'http://scxk.nmpa.gov.cn:81/xk/'
import requests
import json
url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?hKHnQfLv=5pRjC8YQ9WTkmddbznguq71aASHFD4Mn4vb_3f.NOuIRImLZaW2i4SudULEacWMhnRCPnGqwNh01mdwZuwYv4v3JhQr6v4Nd5KX8EJiIe2uTh7ynVpPZhrxVWELmfX5ZOqv3IkflipJWRyqoLDWorNXIEZewQz6VRHS.pf78BWdMuRlQstCiQITOhNwFY4BfUkr.4H7UyuIzxAqV7O7dNHcifUWnT4dIFMt3AzjWbXLkKHReLCGIq_xhid1bFU_GTRcFJRxzbvDX3lnSp0vZpRAHKTjvd5_kWjF8cxVOS8GW&8X7Yi61c=4l97r74gwNat8JFN9LCv2r3q_hpl9RkoRQSSH4wOwyJr7tQDHp85DiG6dTvTfjan4nO8ekHwiI5dp67KUhVMW7zsOA8I23evIFHbBUt78ifBEWseTck4m9_ex0ld.fv.w'
url2= 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?hKHnQfLv=5SJeY07nfh3KtCillk2z99cw0_07ADA9Z0qbuGM5gWOI.Jagaf0yqiB1oYutfzUFR7kNh._rEAwIO3meD1IM2svWcO8sH2nHrFece7btKBY.XLWlGiZWrTjRtLpmX7JmEs0vxcAIUChf2gIvsixG14vylcLD.i8s0.Q_8fJr4zwgBG1abgglnOarFlktMhfMLrBS2Xz9JikiD0Y8dso809cuqK87hGcGmTMFk.33XpCYlKDcOuRzezo0157a3SLGbFudhsN3U5NKyXqu.Y5xu1bfJW7qopbkW3vAt4a4vfggx_t9zxXziLop5wiCe1OZi&8X7Yi61c=42XlTaqg22ci4hrSo8UVBbtr45GR3qaB4E.x1N715mNLetOkr2.Ky6FjQM7ZuXAOFKLL6w57fZlEIk9jxFKCJZnB2sPPhs5O1QeRyjIIbv5tNwUSpgJWZQgzBteE2fZaD'
url3 = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
data={
    'on': 'true',
    'page': '1',
    'pageSize': '15',
    'productName': '',
    'conditionType': '1',
    'applyname': '',
    'applysn': ''
}
id_list=[]
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Safari/537.36'
}

response = requests.post(url=url3,data = data,headers = headers)
json_ids = response.json()
for dic in json_ids['list']:
        id_list.append(dic['ID'])
print(len(id_list))

#
# list_data = response.text

#
# fp = open("./肯德基.json",'w',encoding='utf-8')
#
# json.dump(list_data,fp = fp,ensure_ascii=False)

print("over!!!")

