#include <SoftwareSerial.h>
#include <WiFiEsp.h>
#include <PubSubClient.h>
#include <SimpleTimer.h>
#include <WifiUtil.h>

SoftwareSerial softSerial(2, 3);           // RX, TX

const char ssid[] = "cooluk";               // 네트워크 SSID
const char password[] = "xofla1106!";       // 비밀번호
const char mqtt_server[] = "192.168.0.6"; // 서버 주소

// MQTT용 WiFi 클라이언트 객체 초기화
WifiUtil wifi(2, 3);
WiFiEspClient espClient;
PubSubClient client(espClient);

void callback(char *topic, byte *payload, unsigned int length) {
    payload[length] = NULL;
    char *message = payload;

    if (strcmp("1", message) == 0) {
        digitalWrite(13, HIGH);
    } else {
        digitalWrite(13, LOW);
    }

    Serial.print(topic);
    Serial.print(" : ");
    Serial.println(message);
}

void mqtt_init() {
    client.setServer(mqtt_server, 1883);
    // subscriber인경우 메시지 수신시 호출할 콜백 함수 등록
    client.setCallback(callback);
}

// MQTT 서버에 접속될 때까지 재접속 시도
void reconnect() {

    while (!client.connected()) {
        Serial.print("Attempting MQTT connection...");
        
        if (client.connect("ESP8266Client")) {
            Serial.println("connected");
            // subscriber로 등록
            client.subscribe("home/livingroom/led");  // 구독 신청
        } else {
            Serial.print("failed, rc=");
            Serial.print(client.state());
            Serial.println(" try again in 5 seconds");
            delay(5000);
        }
    }
}

void publish() {
    int state = !digitalRead(13);
    char message[10];
    sprintf(message, "%d", state);

    // 토픽 발행
    client.publish("home/livingroom/led", message);
}

// 2초 간격으로 publish
SimpleTimer timer;

void setup() {
    Serial.begin(9600);
    wifi.init(ssid, password);
    mqtt_init();

    pinMode(13, OUTPUT);
    digitalWrite(13, LOW);
    timer.setInterval(2000, publish);
}

void loop() {
    if (!client.connected()) {  // MQTT가 연결 X
        reconnect();
    }

    client.loop();
    timer.run();
}