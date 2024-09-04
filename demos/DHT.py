import time

import dht
from machine import Pin


def dhtFun():
    dht11 = dht.DHT11(Pin(4))
    dht11.measure()
    print(dht11.temperature(), dht11.humidity())
    time.sleep(0.5)


def main():
    dhtFun()
