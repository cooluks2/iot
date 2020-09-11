int pin_LED = 13;

void setup() {
    Serial.begin(9600);
    pinMode(pin_LED, OUTPUT);
}

void loop() {
    if (Serial.available()) {
        char inChar = Serial.read();
        if (inChar == '\r' || inChar == '\n') return;
        if (inChar == '1') {
            digitalWrite(pin_LED, HIGH);
        } else {
            digitalWrite(pin_LED, LOW);
        }
    }
}