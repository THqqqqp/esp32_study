import time

from machine import Pin, ADC


def do():
    """
    初始化 GPIO15 作为数字输入引脚
    数字输出（DO）引脚提供一个简单的高/低电平信号，这通常表示光强度是否超过了某个预设的阈值（这个阈值可以通过传感器上的电位器进行调节）。
    """
    d_do = Pin(15, Pin.IN)

    d15_value = d_do.value()
    print(d15_value)
    if d15_value == 0:
        print("光线弱")  # 检测到光线弱
    else:
        print("光线强")  # 检测到光线强
    time.sleep(0.5)


def ao():
    """
    初始化 GPIO2 作为模拟输入引脚
    AO 输出的模拟信号是一个连续变化的电压，该信号的大小根据光线强度的变化而变化，ADC 将此信号转换为一个数字值，表示当前的光强度。
    """
    adc = ADC(Pin(2))  # GPIO2 是 ADC1 的通道
    # adc.width(ADC.WIDTH_12BIT)  # 设置 ADC 宽度为 12 位（0-4095）
    # adc.atten(ADC.ATTN_11DB)  # 设置衰减为 11dB，允许输入电压范围为 0-3.6V
    # a_value = adc.read()  # 原始方法读取 ADC1 的值
    a_value = adc.read_u16()  # 读取 ADC1 的值
    print(a_value)
    time.sleep(0.5)


def main():
    do()
    ao()
