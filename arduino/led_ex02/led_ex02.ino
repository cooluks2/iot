int pin_LED = 7;
boolean LED_state = false;

void setup() {
  pinMode(pin_LED, OUTPUT);
  digitalWrite(pin_LED, LED_state);
}

void loop() {
  LED_state = !LED_state;
  digitalWrite(pin_LED, LED_state);
  delay(1000);
}
