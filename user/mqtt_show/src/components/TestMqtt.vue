<script setup>
import {onMounted, ref} from 'vue'
import mqtt from "mqtt";

const msg = ref('ESP32-数据展示')


// MQTT 配置
const brokerUrl = 'ws://localhost:9001'; // WebSocket 连接地址
const topic = 'test/myTestTopic';        // 需要订阅的 MQTT 主题

onMounted(() => {
  // 连接到 MQTT Broker
  const client = mqtt.connect(brokerUrl);

  client.on('connect', () => {
    console.log('Connected to MQTT Broker');
    client.subscribe(topic, (err) => {
      if (!err) {
        console.log(`Subscribed to topic: ${topic}`);
      } else {
        console.error(`Failed to subscribe: ${err.message}`);
      }
    });
  });

  client.on('message', (receivedTopic, message) => {
    if (receivedTopic === topic) {
      msg.value = message.toString();
      console.log(`Received message: ${message.toString()}`);
    }
  });

  // 断开连接处理
  client.on('close', () => {
    console.log('MQTT client disconnected');
  });

  client.on('error', (error) => {
    console.error('MQTT client error:', error);
  });
})
</script>
<template>
  <div>⬇️MQTT实时收到的数据⬇️</div>
  {{ msg }}
</template>
<style scoped>

</style>
