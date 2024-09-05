import paho.mqtt.client as mqtt

# MQTT服务器地址
broker_address = "localhost"  # 替换为你的MQTT代理地址
port = 1883  # MQTT代理的端口，默认为1883
client_id = "python_mqtt_client"  # MQTT客户端的唯一ID，不冲突即可


# 当连接到MQTT代理时调用的回调函数
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # 订阅主题
    client.subscribe("test/myTestTopic")


# 当接收到MQTT消息时调用的回调函数
def on_message(client, userdata, msg):
    print(f"接收到消息： '{msg.payload.decode('utf-8')}',主题： '{msg.topic}'")


# 创建MQTT客户端实例
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# 为客户端设置回调函数
client.on_connect = on_connect
client.on_message = on_message

# 连接到MQTT代理
client.connect(broker_address, port)

# 开始网络循环，处理接收到的消息和重连
client.loop_forever()
