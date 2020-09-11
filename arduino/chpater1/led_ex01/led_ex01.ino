void setup() {
  pinMode(13, OUTPUT);
  digitalWrite(13, false);  // H/F, T/F, 1/0 가능
}

void loop() {
  digitalWrite(13, HIGH);
  delay(300);
  digitalWrite(13, LOW);
  delay(600);
}  // BUILT_IN_LED
