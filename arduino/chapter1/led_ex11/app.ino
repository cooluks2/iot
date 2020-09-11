int pin_LED1 = 7;
int pin_LED2 = 6;
boolean LED_state1 = false;
boolean LED_state2 = false;
unsigned long time_previous1;  // 초기화 되는 첫번째 시간
unsigned long time_current1;  // 현재 시간
unsigned long time_previous2;  // 초기화 되는 첫번째 시간
unsigned long time_current2;  // 현재 시간

void setup() {
    pinMode(pin_LED1, OUTPUT);
    digitalWrite(pin_LED1, LED_state1);
    pinMode(pin_LED2, OUTPUT);
    digitalWrite(pin_LED2, LED_state2);
    Serial.begin(9600);
    time_previous1 = millis();
    time_previous2 = millis();
}

void blink_1000() {
    time_current1 = millis();
    if (time_current1 - time_previous1 >= 1000) {
        time_previous1 = time_current1;  // 1초가 지나고 time_previous를 현재 시간으로 바꿔줌
        LED_state1 = !LED_state1;
        digitalWrite(pin_LED1, LED_state1);
    }
}

void blink_500() {
    time_current2 = millis();
    if (time_current2 - time_previous2 >= 500) {
        time_previous2 = time_current2;
        LED_state2 = !LED_state2;
        digitalWrite(pin_LED2, LED_state2);
    }
}

void loop() {
    blink_1000();
    blink_500();
}