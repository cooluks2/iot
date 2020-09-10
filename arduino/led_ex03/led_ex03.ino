int pin_LED = 7;

void blink(int pin, long time) {
  digitalWrite(pin, HIGH);
  delay(time);
  digitalWrite(pin, LOW);
  delay(time);
}

void setup() {
  pinMode(pin_LED, OUTPUT);
}

void loop() {
  blink(pin_LED, 500);
  blink(pin_LED, 1000);
  blink(pin_LED, 2000);
}
