#include <WiFiEsp.h>
#include <SoftwareSerial.h>

SoftwareSerial softSerial(2, 3); // RX, TX

char ssid[] = "cooluk";        // your network SSID (name)
char pass[] = "xofla1106!";    // your network password
int status = WL_IDLE_STATUS; // the Wifi radio's status

void setup() {
    Serial.begin(115200);
    softSerial.begin(9600);
    WiFi.init(&softSerial);  //주소를 넘긴다.
    // softSerial *p : 포인터로 관리

    if (WiFi.status() == WL_NO_SHIELD) {  // ESP 연결 여부
        Serial.println("WiFi shield not present");
        while (true);  // ESP 가 없으면 진행하지 않는다.
    }

    while (status != WL_CONNECTED) {  // AP 접속 여부
        Serial.print("Attempting to connect to WPA SSID: ");
        Serial.println(ssid);
        status = WiFi.begin(ssid, pass);
    }
    Serial.println("You're connected to the network");
    
    printWifiStatus();
}
void loop() {
}

void printWifiStatus() {

    // print the SSID of the network you're attached to
    Serial.print("SSID: ");
    Serial.println(WiFi.SSID());

    // print your WiFi shield's IP address
    IPAddress ip = WiFi.localIP();
    Serial.print("IP Address: ");
    Serial.println(ip);

    // print the received signal strength
    long rssi = WiFi.RSSI();
    Serial.print("Signal strength (RSSI):");
    Serial.print(rssi);
    Serial.println(" dBm");
}
