#include "WifiUtil.h"

const char SSID[] = "cooluk";
const char PASSWORD[] = "xofla1106!";

WifiUtil wifi(2, 3);

void setup() {
    Serial.begin(9600);
    wifi.init(SSID, PASSWORD);
}

void loop() {
    if (wifi.check()) { // WIFI 연결 확인
        ;
    }
}