# http://www.jianshu.com/p/b036e6e97c18
import asyncio

# Borrowed from http://curio.readthedocs.org/en/latest/tutorial.html.
@asyncio.coroutine
def countdown(number, n):
    while n > 0:
        print('T-minus', n, '({})'.format(number))
        yield from asyncio.sleep(1)
        n -= 1

loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(countdown("A", 2)),
    asyncio.ensure_future(countdown("B", 3))]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


# %%
import time
import asyncio

@asyncio.coroutine
def slow_operation(n):
    yield from asyncio.sleep(1)
    print("Slow operation {} complete".format(n))


@asyncio.coroutine
def main():
    start = time.time()
    yield from asyncio.wait([
        slow_operation(1),
        slow_operation(2),
        slow_operation(3),
    ])
    end = time.time()
    print('Complete in {} second(s)'.format(end-start))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

# %%
import asyncio
import time

async def slow_operation(n):
    await asyncio.sleep(1)
    print("Slow operation {} complete".format(n))


async def main():
    start = time.time()
    await asyncio.wait([
        slow_operation(1),
        slow_operation(2),
        slow_operation(3),
    ])
    end = time.time()
    print('Complete in {} second(s)'.format(end-start))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

# %%
import asyncio
import time

async def slow_operation(n):
    await asyncio.sleep(1)
    # time.sleep(1)
    print("Slow operation {} complete".format(n))

async def another_operation(n):
    await asyncio.sleep(1)
    print("Another operation {} complete".format(n))

async def main():
    start = time.time()
    sub_threads = [slow_operation(i) for i in range(1,4)]
    sub_threads.append(another_operation(5))
    await asyncio.wait(sub_threads)
    end = time.time()
    print('Complete in {} second(s)'.format(end-start))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

# %%
import asyncio
import requests
import time

# 这里用request不能实现异步，需要用aiohttp才行，参考async_await.py
async def download(url): # 通过async def定义的函数是原生的协程对象
    response = requests.get(url)
    print(response.text)


async def wait_download(url):
    await download(url) # 这里download(url)就是一个原生的协程对象
    print("get {} data complete.".format(url))


async def main():
    start = time.time()
    await asyncio.wait([
        wait_download("http://www.163.com"),
        wait_download("http://www.qq.com"),
        wait_download("http://www.sohu.com")])
    end = time.time()
    print("Complete in {} seconds".format(end - start))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
