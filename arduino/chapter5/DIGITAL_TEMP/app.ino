int Led = 13;      // define LED Interface
int buttonpin = 3; // define the digital temperature sensor interface
int val; // define numeric variables val
void setup()
{
    pinMode(Led, OUTPUT);
    pinMode(buttonpin, INPUT);
}
void loop()
{
    val = digitalRead(buttonpin);
    if (val == HIGH)
    {
        digitalWrite(Led, HIGH);
    }
    else
    {
        digitalWrite(Led, LOW);
    }
}