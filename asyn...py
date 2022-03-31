import asyncio
import aiohttp



async def coro1():
    while True:
        await asyncio.sleep(0.02)
        print("Coro 1 Working!")


async def coro2():
    while True:
        await asyncio.sleep(0.01)
        print("Coro 22222222 Working!")


async def coro3():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://py4you.com/') as response:
            status_code = response.status
            read = await response.read()
            print(f'Status code = {status_code}')
            print(read)

#async def main():
   # task1 = coro1()
    #task2 = coro2()
    #await asyncio.gather(task1, task2)


#asyncio.run(main())
runer = asyncio.gather(coro3())
loop = asyncio.get_event_loop()
loop.run_until_complete(runer)
