import uasyncio as asyncio

import demos.DHT as DHT
import demos.MH as MH


# 定义异步函数来读取 MH 传感器数据
async def read_mh():
    while True:
        MH.main()
        await asyncio.sleep(1)  # 使用 await asyncio.sleep 来替代 time.sleep


# 定义异步函数来读取 DHT 传感器数据
async def read_dht():
    while True:
        DHT.main()
        await asyncio.sleep(1)


# 主函数
async def main():
    print("system start...")

    # 创建任务并发执行
    mh_task = asyncio.create_task(read_mh())
    dht_task = asyncio.create_task(read_dht())

    await mh_task
    await dht_task


if __name__ == '__main__':
    # 启动异步事件循环
    asyncio.run(main())
