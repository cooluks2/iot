int pin_LED = 13;
boolean LED_state = false;
unsigned long time_previous;  // 초기화 되는 첫번째 시간
unsigned long time_current;  // 현재 시간
unsigned long count = 0;

void setup() {
    pinMode(pin_LED, OUTPUT);
    digitalWrite(pin_LED, LED_state);
    Serial.begin(9600);
    time_previous = millis();
}

void loop() {
    time_current = millis();
    count++;

    // 1초 이상 시간이 경과한 경우
    if (time_current - time_previous >= 1000) {
        time_previous = time_current;

        LED_state = !LED_state;
        digitalWrite(pin_LED, LED_state);
        
        Serial.println(count);
        count = 0;
    }
}