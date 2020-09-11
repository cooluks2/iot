int pin_LED1 = 7;
int pin_LED2 = 8;

void setup() {
  pinMode(pin_LED1, OUTPUT);
  pinMode(pin_LED2, OUTPUT);
  digitalWrite(pin_LED1, LOW);
  digitalWrite(pin_LED2, LOW);
}

void loop() {
  digitalWrite(pin_LED1, HIGH);
  delay(500);
  digitalWrite(pin_LED1, LOW);
  digitalWrite(pin_LED2, HIGH);
  delay(500);
  digitalWrite(pin_LED1, HIGH);
  delay(500);
  digitalWrite(pin_LED1, LOW);
  digitalWrite(pin_LED2, LOW);
  delay(500);
}
