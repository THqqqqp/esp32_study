<script setup>
import Msg from './components/Msg.vue'
import TestMqtt from './components/TestMqtt.vue'
import {onMounted, reactive, ref} from 'vue'
import * as echarts from 'echarts'

const chart1 = ref(null)
const chart1_Option = reactive({
  xAxis: {
    type: 'category',
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      data: [150, 230, 224, 218, 135, 147, 260],
      type: 'line'
    }
  ]
})

const chart2 = ref(null)
const chart2_Option = reactive({
  tooltip: {
    formatter: '{a} <br/>{b} : {c}%'
  },
  series: [
    {
      type: 'gauge',
      center: ['50%', '60%'],
      startAngle: 200,
      endAngle: -20,
      min: 0,
      max: 60,
      splitNumber: 12,
      itemStyle: {
        color: '#FFAB91'
      },
      progress: {
        show: true,
        width: 30
      },
      pointer: {
        show: false
      },
      axisLine: {
        lineStyle: {
          width: 30
        }
      },
      axisTick: {
        distance: -45,
        splitNumber: 5,
        lineStyle: {
          width: 2,
          color: '#999'
        }
      },
      splitLine: {
        distance: -52,
        length: 14,
        lineStyle: {
          width: 3,
          color: '#999'
        }
      },
      axisLabel: {
        distance: -20,
        color: '#999',
        fontSize: 20
      },
      anchor: {
        show: false
      },
      title: {
        show: false
      },
      detail: {
        valueAnimation: true,
        width: '60%',
        lineHeight: 40,
        borderRadius: 8,
        offsetCenter: [0, '-15%'],
        fontSize: 40,
        fontWeight: 'bolder',
        formatter: '{value}°C',
        color: 'inherit'
      },
      data: [
        {
          value: 20
        }
      ]
    },
    {
      type: 'gauge',
      center: ['50%', '60%'],
      startAngle: 200,
      endAngle: -20,
      min: 0,
      max: 60,
      itemStyle: {
        color: '#FD7347'
      },
      progress: {
        show: true,
        width: 8
      },
      pointer: {
        show: false
      },
      axisLine: {
        show: false
      },
      axisTick: {
        show: false
      },
      splitLine: {
        show: false
      },
      axisLabel: {
        show: false
      },
      detail: {
        show: false
      },
      data: [
        {
          value: 20
        }
      ]
    }
  ]
})

onMounted(() => {
  const myChart1 = echarts.init(chart1.value)
  const myChart2 = echarts.init(chart2.value)
  myChart1.setOption(chart1_Option)
  myChart2.setOption(chart2_Option)

  setInterval(() => {
    //   定时修改myChart2的data值,一位数据
    let a = parseFloat((Math.random() * 60).toFixed(1))
    chart2_Option.series.map(i => {
      i.data[0].value = a
    })
    myChart2.setOption(chart2_Option)
  }, 1000)
})
</script>

<template>
  <Msg msg="ESP32-数据展示"/>
  <view style="display: flex;gap: 30px">
    <div ref="chart1" style="width: 400px;height: 300px;border: 1px solid red"></div>
    <div ref="chart2" style="width: 400px;height: 300px;border: 1px solid red"></div>
  </view>
  <TestMqtt/>
</template>

<style scoped>
</style>
