int led = 8;
void setup()
{
    pinMode(led, OUTPUT);
}
void loop()
{
    digitalWrite(led, HIGH); // set the LED on
    delay(2000);             // wait for a second
    digitalWrite(led, LOW);  // set the LED off
    delay(2000);             // wait for a second
}