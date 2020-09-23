const int pin_button = 11;
long startTime = 0;
long swCountTimer = 0;

void setup() {
    Serial.begin(9600);
    pinMode(pin_button, INPUT_PULLUP);
}

void loop() {
    if(digitalRead(pin_button) == LOW) { // 스위치가 눌러진 경우
        startTime = millis(); // 현재 시간 측정
        while(digitalRead(pin_button) == LOW); // 눌러진 시간 동안 지연
        
        // 스위치를 뗀 시간을 측정하여 차이 계산
        swCountTimer = millis() - startTime;
        
        Serial.print(swCountTimer);
        Serial.println(" ms");
    }
}