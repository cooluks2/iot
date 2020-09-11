int leds[] = {3,5,6};

void setup() {
    for(auto &pin : leds) {
        pinMode(pin, OUTPUT);
    }
}

void fade(int pin) {
    for(int i=0; i<=255; i++) {
        analogWrite(pin, i);
        delay(10);
    }
    for(int i=255; i>=0; i--) {
        analogWrite(pin, i);
        delay(10);
    }
}

void loop() {
    for(auto &pin : leds) {
        fade(pin);
    }
}