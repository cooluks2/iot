#include <DHT.h> // DHT.h 라이브러리를 포함한다

#define DHTPIN 3
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE); // DHT설정 - dht (디지털3, dht11)

void setup() {
    Serial.begin(9600); // 9600 속도로 시리얼 통신을 시작한다
    dht.begin();
}

void loop() {
    delay(2000);
    // LCD는 float 출력을 못한다.
    float h = dht.readHumidity();    // 변수 h에 습도 값을 저장
    float t = dht.readTemperature(); // 변수 t에 온도 값을 저장

    Serial.print("Humidity: ");
    Serial.print(h);
    Serial.print("%\t");
    Serial.print("Temperature: ");
    Serial.print(t);
    Serial.println(" C");
}