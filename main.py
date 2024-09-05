import time

import network
import uasyncio as asyncio
from umqtt.simple import MQTTClient

import demos.DHT as DHT
import demos.MH as MH


# 光敏
async def read_mh():
    while True:
        MH.main()
        await asyncio.sleep(1)  # 使用 await asyncio.sleep 来替代 time.sleep


# 温湿度
async def read_dht():
    while True:
        DHT.main()
        await asyncio.sleep(1)


# 连接Wi-Fi
def connect_wifi(ssid, password):
    # 初始化 STA（Station）模式
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    # 检查是否已经连接
    if not wlan.isconnected():
        print('Connecting to network...')
        wlan.connect(ssid, password)

        # 等待连接成功
        while not wlan.isconnected():
            print('Waiting for connection...')
            time.sleep(1)

    print('Network connected:', wlan.ifconfig())


# 配置MQTT
def config_mqtt(mqtt_server='localhost'):
    client_id = 'esp32-client'
    topic_pub = 'test/myTestTopic'

    client = MQTTClient(client_id, mqtt_server)
    client.connect()

    num = 0

    while True:
        num += 1
        msg = f'num:{num}'
        client.publish(topic_pub, msg)
        print("Sent:", msg)
        time.sleep(5)


# 主函数
async def main():
    print("system start...")

    connect_wifi('INET', 'INet1529st')

    config_mqtt('192.168.1.102')

    # 创建任务并发执行
    mh_task = asyncio.create_task(read_mh())
    dht_task = asyncio.create_task(read_dht())

    # await mh_task
    # await dht_task


if __name__ == '__main__':
    # 启动异步事件循环
    asyncio.run(main())
