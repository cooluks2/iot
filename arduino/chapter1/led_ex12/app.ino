int pin_LED1 = 7;
int pin_LED2 = 6;

boolean LED_state1 = false;
boolean LED_state2 = false;

void setup() {
    pinMode(pin_LED1, OUTPUT);
    pinMode(pin_LED2, OUTPUT);

    digitalWrite(pin_LED1, LOW);
    digitalWrite(pin_LED2, LOW);
}

void loop() {
    blink_led1();
    blink_led2();
}

void blink_led1() {
    static unsigned long time_previous = 0;
    const int INTERVAL = 500;
    unsigned long time_current = millis();

    if (time_current - time_previous > INTERVAL) {
        time_previous = time_current;
        LED_state1 = !LED_state1;
        digitalWrite(pin_LED1, LED_state1);
    }
}

void blink_led2() {
    static unsigned long time_previous = 0;
    const int INTERVAL = 1000;
    unsigned long time_current = millis();
    
    if (time_current - time_previous > INTERVAL) {
        time_previous = time_current;
        LED_state2 = !LED_state2;
        digitalWrite(pin_LED2, LED_state2);
    }
}