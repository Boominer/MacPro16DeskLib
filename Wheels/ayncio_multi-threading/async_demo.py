import asyncio
from time import sleep, perf_counter
import aiohttp
import aiofiles

"""
Url - https://www.bilibili.com/video/BV157mFYEEkH?spm_id_from=333.788.videopod.sections&vd_source=3e0ea0bcb977cb8d47f4451ff8c0e242
携程的英文是 coroutine，协程的意思
携程的最主要的特点是，可以暂停执行，然后恢复执行，这样就可以实现异步编程，而不需要使用多线程。

1. 用async def 定义携程函数
2. 创建携程对象，使用 asyncio.create_task 或 asyncio.gather 或 asyncio.as_completed
3. 使用 await 等待携程对象完成
4. 使用 asyncio.run 运行携程函数
"""

async def fetch_url(url):
    print("Fetching the URL")
    await asyncio.sleep(1)
    print("Finished fetching")
    return "url_content"

async def read_file(filepath):
    print("Reading the file")
    await asyncio.sleep(1)
    print("Finished reading")
    return "file_content"

async def main():
    url = "example.com"
    filepath = "example.text"

    # 手动创建任务，并等待它们完成
    # task1 = asyncio.create_task(fetch_url(url))
    # task2 = asyncio.create_task(read_file(filepath))
    # fetch_result = await task1
    # read_result = await task2

    # 自动返回携程对象，并等待它们完成 using asyncio.gather
    # results = await asyncio.gather(fetch_url(url), read_file(filepath))
    # print(results)
    
    # 自动返回携程对象，并等待它们完成 using asyncio.as_completed
    results = await asyncio.as_completed([fetch_url(url), read_file(filepath)])
    for result in results:
        print(await result)

if __name__ == "__main__":
    start_time = perf_counter()
    asyncio.run(main())
    end_time = perf_counter()
    print(f"Time taken: {end_time - start_time:.2f} seconds")