import paho.mqtt.client as mqtt
from time import sleep
from random import random

# 1. MQTT 클라이언트 객체 인스턴스화
client = mqtt.Client()

try :
    # 2. 브로커 연결
    client.connect("localhost")
    
    # 3. 토픽 메시지 발행
    while True:
        client.publish("iot/home2/temp", 25+random())
        client.loop(2)
        sleep(2)
except Exception as err:
	print('에러 : %s'%err)