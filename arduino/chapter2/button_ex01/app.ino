int LED = 4;
int BUTTON = 11;
void setup()
{
    pinMode(BUTTON, INPUT);
    pinMode(LED, OUTPUT);
}
void loop()
{
    if (digitalRead(BUTTON))
    { // 누른 경우
        digitalWrite(LED, HIGH);
    }
    else
    {
        digitalWrite(LED, LOW);
    }
    delay(10);
}