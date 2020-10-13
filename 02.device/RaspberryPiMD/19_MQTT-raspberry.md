# MQTT - raspberry

$ `sudo apt install mosquitto mosquitto-clients`

$ `sudo pip3 install paho-mqtt`

$ `ps` : 현재 터미널에서 실행 중인 프로그램 확인

$ `ps -elf` : 현재 동작하는 모든 프로그램 확인

$ `ps -elf | grep mosq` : mosq 단어가 들어있는 라인 필터링

---

PYMONGO-EX 폴더 P:\workspace\09_PYMONGO-EX로 이동

$ `pip install pymongo`

<br>

**MongoDB 설정 서비스 등록**

C:\Program Files\MongoDB\Server\4.4\bin\mongod.cfg 파일 C:\data 로 이동

`명령 프롬프트` > 관리자 권한으로 실행

\> `mongod --install --config C:\data\mongod.cfg`

`서비스` > `MongoDB` >`시작`

`robo3t` > ip로 접속 가능 확인

<br>

**Publisher - 아두이노** DHT

mqtt/app.ino

```cpp
#include <SoftwareSerial.h>
#include <WiFiEsp.h>
#include <PubSubClient.h>
#include <SimpleTimer.h>
#include <WifiUtil.h>
#include <DHT.h>
#include <MiniCom.h>

SoftwareSerial softSerial(2, 3);           // RX, TX

const char ssid[] = "cooluk";               // 네트워크 SSID
const char password[] = "xofla1106!";       // 비밀번호
const char mqtt_server[] = "192.168.0.10"; // 라즈베리파이의 브로커 주소

unsigned long lowpulseoccupancy = 0;
float ratio = 0;

MiniCom com;
DHT dht(4, DHT11); // DHT설정 - dht (디지털3, dht11)
const int DUST_PIN = 8;
unsigned long sampletime_ms = 2000;

// MQTT용 WiFi 클라이언트 객체 초기화
WifiUtil wifi(2, 3);
WiFiEspClient espClient;
PubSubClient client(espClient);

void mqtt_init() {
    client.setServer(mqtt_server, 1883);
}

// MQTT 서버에 접속될 때까지 재접속 시도
void reconnect() {

    while (!client.connected()) {
        Serial.print("Attempting MQTT connection...");
        
        if (client.connect("ESP8266Client")) {
            Serial.println("connected");
            // subscriber로 등록
            client.subscribe("home/home1/#");  // 구독 신청
        } else {
            Serial.print("failed, rc=");
            Serial.print(client.state());
            Serial.println(" try again in 5 seconds");
            delay(5000);
        }
    }
}

void publish() {
    float h = dht.readHumidity();
    float t = dht.readTemperature();
    char message[10];
    // 토픽 발행
    dtostrf(h, 5, 2, message);
    client.publish("iot/home1/humi", message);
    dtostrf(t, 5, 2, message);
    client.publish("iot/home1/temp", message);

    com.print(0, "humi", h);
    com.print(1, "temp", t);
    Serial.print(h);
    Serial.print(",");
    Serial.println(t);
}

// 2초 간격으로 publish
// SimpleTimer timer;

void setup() {
    com.init();
    wifi.init(ssid, password);
    mqtt_init();
    dht.begin();
    pinMode(DUST_PIN, INPUT);
    com.setInterval(2000,publish);
}

void loop() {
    unsigned long start = millis();
    if (!client.connected()) {  // MQTT가 연결 X
        reconnect();
    }

    client.loop();
    com.run();
    // timer.run();
    unsigned long end = millis();
    Serial.println(end-start);
}
```

<br>

**Subscriber - 라즈베리파이**

Subscriber.py (기존 작성)

```python
import paho.mqtt.client as mqtt
from pymongo import MongoClient
from datetime import datetime

mongodb = MongoClient("mongodb://192.168.0.11:27017/")
db = mongodb.iot_service

# 브로커 접속 시도 결과 처리 콜백 함수
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+ str(rc))
    if rc == 0:
        client.subscribe("iot/#") # 연결 성공시 토픽 구독 신청
    else:
        print('연결 실패 : ', rc)
        
# 관련 토픽 메시지 수신 콜백 함수
def on_message(client, userdata, msg):
    value = float(msg.payload.decode())
    print(f" {msg.topic} {value}")
    # MongoDB에 데이터 저장하는 코드가 여기에서 이루어짐
    doc = {
        "topic" : msg.topic,
        "value" : value,
        "reg_date" : datetime.now()
    }
    db.sensors.insert_one(doc)
    
# 1. MQTT 클라이언트 객체 인스턴스화
client = mqtt.Client()

# 2. 관련 이벤트에 대한 콜백 함수 등록
client.on_connect = on_connect
client.on_message = on_message

try :
    # 3. 브로커 연결
    client.connect("localhost")
    
    # 4. 메시지 루프 - 이벤트 발생시 해당 콜백 함수 호출됨
    client.loop_forever()

    # client.loop_start()
    # 새로운 스래드를 가동해서 운영 - daemon 스레드  Thread.setDaemon(True)
except Exception as err:
	print('에러 : %s'%err)
    
print("--- End Main Thread ---")
```



Robo 3T

![image-20201013152212318](19_MQTT-raspberry.assets/image-20201013152212318.png)  