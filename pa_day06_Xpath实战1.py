import requests
from lxml import etree

if __name__ == "__main__":

    url = 'https://sh.58.com/ershoufang/?PGTID=0d200001-0000-2fa2-68a3-b084feebf128&ClickID=1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        'cookie':'f=n; commontopbar_new_city_info=2%7C%E4%B8%8A%E6%B5%B7%7Csh; time_create=1658384394297; userid360_xml=B40F16E56A86E56943464C3B3EEF0EE5; SECKEY_ABVK=qqjiJWL4u8WlDP3duH8mqnGSEYtX+aqdyoMKurt6cPs%3D; BMAP_SECKEY=lQGdV6eTZ6n_-_Q-GyZUOqos8HbfuW89ebb29DlSip4vMOtG7bzU1cEzfZWlfaw_7ll1AYHz5xaCWWvFk0Iz22QyWzj6RwxBfCXeU-DBXbVr2fXMJhyU7M5FBvDgoW7SQkaAD8eXeoGD4Vj3QxrWKSLh8LsRaHD7SuG1WSFyOoVtb4c5FwRE20v72qZSMr-Y; myLat=""; myLon=""; id58=XthNKWKxYuqczbiw8RFd9g==; mcity=sh; f=n; 58home=sh; city=sh; commontopbar_new_city_info=2%7C%E4%B8%8A%E6%B5%B7%7Csh; 58tj_uuid=d3a7059c-9d20-48ef-9e98-1e2a4504b780; new_uv=1; utm_source=market; spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT; init_refer=https%253A%252F%252Fwww.baidu.com%252Fother.php%253Fsc.0f0000afQS3xb5jhWLktIAjnOe511ByS9tG2HPsk1VRkXtgzhpjeI9amk53VECkXrwjnYchXK2B_WbXfVQRxlNTcTNlJCjW6P7ztIcTy1NBzztrEIkBrwsQUOr6oZa1N1HZLEO1R4rtBJqTxz5EKed8UtM5iu7KThBOTCRbvReQOc038PPLekodiCLhcE1sKB-3uL0HtNBZqmaJS02fsxjDBIsdJ.DY_NR2Ar5Od66z3PrrW6ButVvkDj3n-vHwYxw_vU85YIMAQV8qhORGyAp7WIu8L6.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqPHWPoQ5Z0ZN1ugFxIZ-suHYs0A7bgLw4TARqnsKLULFb5HR31pz1ksKzmLmqn0KdThkxpyfqnHR1PW64PWfzr0KVINqGujYkPjmsPHD3PfKVgv-b5HDkPWc1PHDL0AdYTAkxpyfqnHc3nWm0TZuxpyfqn0KGuAnqHbG2RsKspyfqn6KWpyfqPj0s0APzm1YznjT3P0%2526dt%253D1655792359%2526wd%253D58%2525E5%252; als=0; commontopbar_ipcity=sh%7C%E4%B8%8A%E6%B5%B7%7C0; wmda_uuid=fcfc4903d064fee81a20d8e0ca9f4ec8; wmda_new_uuid=1; wmda_session_id_11187958619315=1655792366013-deb76b93-05c0-630e; new_session=0; wmda_session_id_2385390625025=1655792366838-df3347ef-a656-4f40; wmda_visited_projects=%3B11187958619315%3B2385390625025; xxzl_deviceid=FvwtGgs469AYmldMleDmUtM94oHRnepjfhHX8IkT259%2FDxT6MF5HDd9mzt9b396r; aQQ_ajkguid=132BA715-BF11-4137-AA12-41DF0A60CAF9; sessid=7B9B29B4-90EE-4619-B898-CEF2962AF696; ajk-appVersion=; fzq_h=21808221fde1ef0480d0095c32d89cc0_1655792386926_a0f4c3fdab26463cb1be12cb4f9c1161_3662792216; 58_ctid=2; is_58_pc=1; commontopbar_new_city_info=11%7C%E4%B8%8A%E6%B5%B7%7Csh; ctid=2; ipcity=sh%7C%u4E0A%u6D77; myfeet_tooltip=end; xxzl_cid=451647b6f2e24765ab62db49be8516ee; xzuid=5d43fbd1-cff8-4015-8bb4-068c17824cd4'
    }
    htmlText = requests.get(url,headers = headers).text
    selector = etree.HTML(htmlText)
    title = selector.xpath('//h3/text()')[0]
    print(title)
