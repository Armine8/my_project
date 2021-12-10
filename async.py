
import asyncio
from urllib.request import urlopen

import aiohttp
import gevent as gevent

URLS = ['http://127.0.0.1:8000/categories/2', 'http://127.0.0.1:8000/categories/3', 'http://127.0.0.1:8000/categories/5']


def get_data(URL):
    data = urlopen(URL).read()
    file = open("my_file.txt", "w")
    file.write(f'{data}')
    file.close()
    print(f'resp:{len(data)}')
async def main():
    async with aiohttp.ClientSession() as session:
        for url in URLS:
            print(url)
            async with session.get(url) as response:
                print("Status:", response.status)
                print("Content-type:", response.headers['content-type'])

                html = await response.text()
                file = open("data.txt", "w")
                file.write(f'{html}')
                file.close()
                print("Body:", html[:15], "...")

prod = [gevent.spawn(get_data, u) for u in URLS]
gevent.wait(prod)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())