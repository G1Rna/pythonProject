import aiohttp
import requests
import asyncio
import time
import aiohttp
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    }
async def request(url):
    #以下用的异步方法获取相应url
    async with aiohttp.ClientSession() as session:
        # headers.params/data.proxy='https://ip:port' #设置代理参数
        async with await session.get(url) as response:
             code = await response.text()
    await asyncio.sleep(2)
    print(f'访问完毕')

def res(url):
    code = requests.get(url = url, headers = headers).status_code #requests.get也是同步的
    time.sleep(2)
    print(f'访问完毕')

if __name__ == '__main__':

    urls = {
        'https://www.baidu.com/',
        'https://www.bilibili.com/'
    }
    stasks = []
    for url in urls:
        c = request(url)
        task = asyncio.ensure_future(c)
        stasks.append(task)

    print("-----异步-----")
    start = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(stasks))
    end = time.time()
    print('总计用时:'+str(end-start))

    print("-----同步-----")
    start1 = time.time()
    for url in urls:
        c1 = res(url)
    end1 = time.time()
    print('总计用时:' + str(end1 - start1))