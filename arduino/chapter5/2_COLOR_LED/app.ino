int redpin = 10;  // select the pin for the red LED
int bluepin = 11; // select the pin for the blueLED
int val;
void setup()
{
    pinMode(redpin, OUTPUT);
    pinMode(bluepin, OUTPUT);
}
void loop()
{
    for (val = 255; val > 0; val--)
    {
        analogWrite(redpin, val);
        analogWrite(bluepin, 255 - val);
        delay(15);
    }
    for (val = 0; val < 255; val++)
    {
        analogWrite(redpin, val);
        analogWrite(bluepin, 255 - val);
        delay(15);
    }
}