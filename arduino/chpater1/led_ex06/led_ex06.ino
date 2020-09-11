int pin_LED1 = 8;
int pin_LED2 = 7;
int pin_LED3 = 6;

void setup() {
  pinMode(pin_LED1, OUTPUT);
  pinMode(pin_LED2, OUTPUT);
  pinMode(pin_LED3, OUTPUT);
}

void loop() {
  digitalWrite(pin_LED1, HIGH);
  delay(2000);
  digitalWrite(pin_LED1, LOW);
  digitalWrite(pin_LED2, HIGH);
  delay(1000);
  digitalWrite(pin_LED2, LOW);
  digitalWrite(pin_LED3, HIGH);
  delay(2000);
  digitalWrite(pin_LED3, LOW);
}
