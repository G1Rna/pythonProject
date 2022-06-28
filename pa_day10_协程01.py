
import asyncio
import time

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    }
async def request(url):

    # time.sleep(2) #异步协程中如果出现了同步的代码，则无法实现效果
    await asyncio.sleep(2)#使用异步阻塞的代码
    print(f'访问完毕')

def res(url):
    time.sleep(2) #异步协程中如果出现了同步的代码，则无法实现效果
    print(f'访问完毕')

if __name__ == '__main__':
    start = time.time()
    urls = {
        'https://www.baidu.com/',
        'https://www.bilibili.com/'
    }
    stasks = []
    for url in urls:
        c = request(url)
        task = asyncio.ensure_future(c)
        stasks.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(stasks))

    end = time.time()
    print('总计用时:'+str(end-start))


    print("-----同步-----")
    start1 = time.time()

    stasks = []
    for url in urls:
        c1 = res(url)

    end1 = time.time()
    print('总计用时:' + str(end1 - start1))