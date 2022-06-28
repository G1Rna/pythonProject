import requests

#自定义请求
purl = 'https://member1.taobao.com/member/fresh/account_security.htm?spm=a1z09.8149145.754894437.3.6d802c9cNMzQk9'
# purl = 'https://baidu.com'
#headers 请求伪装
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
#     'cookie':'cna=1/d/GPHlhRoCAbSkmEurRAdE; enc=X2I8v9kGly2PRIswyde%2F1xGWuPv1QudrnXv9NYkjO1q0NPNyvMKAEqApEpT0xIJxCRUsQAaozRVAwnnjrzWHtg%3D%3D; miid=229095011751200923; _m_h5_tk=5ab1be330a22878722fb220627b46698_1655096700483; _m_h5_tk_enc=f5a7b6a39527764d560c81c977b07f62; cookie2=1ca2b2229f917cf53503742518e2340d; t=bc9015581a118031e35bafbac09fa5a3; _tb_token_=58e39e3e83de; _samesite_flag_=true; xlly_s=1; sgcookie=E100Y6J65Ncvd4Uj8%2FEQfiKUqNacYldLSHS6qBcPsR4Sovm3mp8pTz7f4XWmcn7OioD8iJbm%2F9oSM983rb4kuLWZcpKqtg7YQkxB0g98OdLdA7tPrCgqtUPW1xD385vyr9mI; unb=1934131853; uc3=nk2=0R%2BWJACf&lg2=VFC%2FuZ9ayeYq2g%3D%3D&id2=UojXLDw2D8pkWA%3D%3D&vt3=F8dCvC3woHdIFZalX1k%3D; csg=8ad9c6bb; lgc=%5Cu8349%5Cu4E1B%5Cu6851; cancelledSubSites=empty; cookie17=UojXLDw2D8pkWA%3D%3D; dnk=%5Cu8349%5Cu4E1B%5Cu6851; skt=ec168f7a1446dc97; existShop=MTY1NTA4ODQzOA%3D%3D; uc4=id4=0%40UOBTfuj0Ub3oNmAFryngPLwTAYJS&nk4=0%400yc0wkSIjso73Z3unIz9dhI%3D; tracknick=%5Cu8349%5Cu4E1B%5Cu6851; _cc_=V32FPkk%2Fhw%3D%3D; _l_g_=Ug%3D%3D; sg=%E6%A1%9133; _nk_=%5Cu8349%5Cu4E1B%5Cu6851; cookie1=AiA1dKdWEdFLBJ4wb9v6%2BjmabYDyKu%2BdECuCdZ3Qfvg%3D; mt=ci=4_1; thw=cn; uc1=cookie14=UoexN9Mfrj8z6w%3D%3D&cookie15=UIHiLt3xD8xYTw%3D%3D&pas=0&existShop=false&cart_m=0&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&cookie21=UtASsssmeW6lpyd%2BBROh; isg=BCgoh0aT3m27HPBqzMVu9zmF-RY6UYxbHQ9mG-JZdKOWPcinimFc675_NdXNFkQz; l=eBr_-2X4jxwB38UbBOfanurza77OSIRYYuPzaNbMiOCP_2CB5gSCW6jri4L6C3GVh6vvR3lFyc9kBeYBqQAonxvOUKaOYMkmn; tfstk=c3kcB09fEjPfiNVoOKwXBjQJhkvdwyBa-AkSUnk11PtfPaCcQ_5UHQKuoeTV1'
# }


headers = {
    'authority': 'member1.taobao.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Aoyou/DW5ZPEVrKWUgJGU4b3UkYOI-tyJdCRWSCUmFvkPvu4w0npSe-kPmnxz73A==',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://buyertrade.taobao.com/',
    'accept-language': 'zh-CN,zh;q=0.9',
     'cookie':'cna=1/d/GPHlhRoCAbSkmEurRAdE; enc=X2I8v9kGly2PRIswyde%2F1xGWuPv1QudrnXv9NYkjO1q0NPNyvMKAEqApEpT0xIJxCRUsQAaozRVAwnnjrzWHtg%3D%3D; miid=229095011751200923; _m_h5_tk=5ab1be330a22878722fb220627b46698_1655096700483; _m_h5_tk_enc=f5a7b6a39527764d560c81c977b07f62; cookie2=1ca2b2229f917cf53503742518e2340d; t=bc9015581a118031e35bafbac09fa5a3; _tb_token_=58e39e3e83de; _samesite_flag_=true; xlly_s=1; sgcookie=E100Y6J65Ncvd4Uj8%2FEQfiKUqNacYldLSHS6qBcPsR4Sovm3mp8pTz7f4XWmcn7OioD8iJbm%2F9oSM983rb4kuLWZcpKqtg7YQkxB0g98OdLdA7tPrCgqtUPW1xD385vyr9mI; unb=1934131853; uc3=nk2=0R%2BWJACf&lg2=VFC%2FuZ9ayeYq2g%3D%3D&id2=UojXLDw2D8pkWA%3D%3D&vt3=F8dCvC3woHdIFZalX1k%3D; csg=8ad9c6bb; lgc=%5Cu8349%5Cu4E1B%5Cu6851; cancelledSubSites=empty; cookie17=UojXLDw2D8pkWA%3D%3D; dnk=%5Cu8349%5Cu4E1B%5Cu6851; skt=ec168f7a1446dc97; existShop=MTY1NTA4ODQzOA%3D%3D; uc4=id4=0%40UOBTfuj0Ub3oNmAFryngPLwTAYJS&nk4=0%400yc0wkSIjso73Z3unIz9dhI%3D; tracknick=%5Cu8349%5Cu4E1B%5Cu6851; _cc_=V32FPkk%2Fhw%3D%3D; _l_g_=Ug%3D%3D; sg=%E6%A1%9133; _nk_=%5Cu8349%5Cu4E1B%5Cu6851; cookie1=AiA1dKdWEdFLBJ4wb9v6%2BjmabYDyKu%2BdECuCdZ3Qfvg%3D; mt=ci=4_1; thw=cn; uc1=cookie14=UoexN9Mfrj8z6w%3D%3D&cookie15=UIHiLt3xD8xYTw%3D%3D&pas=0&existShop=false&cart_m=0&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&cookie21=UtASsssmeW6lpyd%2BBROh; isg=BCgoh0aT3m27HPBqzMVu9zmF-RY6UYxbHQ9mG-JZdKOWPcinimFc675_NdXNFkQz; l=eBr_-2X4jxwB38UbBOfanurza77OSIRYYuPzaNbMiOCP_2CB5gSCW6jri4L6C3GVh6vvR3lFyc9kBeYBqQAonxvOUKaOYMkmn; tfstk=c3kcB09fEjPfiNVoOKwXBjQJhkvdwyBa-AkSUnk11PtfPaCcQ_5UHQKuoeTV1'
}

res=requests.get(url = purl ,headers = headers)

code = res.status_code
print(code)
if(code == 200):
    with open('./test.html','wb') as fp:
        fp.write(res.text.encode('utf-8'))