import requests
import json
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
data={
    'cname':'',
    'pid':'',
    'keyword': '徐泾',
    'pageIndex': '1',
    'pageSize': '10',
}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Safari/537.36'
}

response = requests.post(url=url,data = data,headers = headers)

list_data = response.text

fp = open("./肯德基.json",'w',encoding='utf-8')

json.dump(list_data,fp = fp,ensure_ascii=False)

print("over!!!")

