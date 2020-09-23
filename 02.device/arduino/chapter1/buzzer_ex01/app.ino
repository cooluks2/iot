int buzzerPin = 5;
void setup()
{
    pinMode(buzzerPin, OUTPUT);
}
void loop() {
    digitalWrite(buzzerPin,HIGH);
    delay(50);
    digitalWrite(buzzerPin,LOW);
    delay(400);
}