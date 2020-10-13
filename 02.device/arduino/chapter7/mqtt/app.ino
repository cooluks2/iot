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