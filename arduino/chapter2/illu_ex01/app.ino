int pSensor = A0;
int ledPin = 3;
void setup()
{
    Serial.begin(9600);
    pinMode(ledPin, OUTPUT);
}
void loop()
{
    int readVal = analogRead(pSensor);
    Serial.print("Read Value = ");
    Serial.println(readVal);
    if (readVal < 200)
    { // 어두워지면 LED 켜기
        digitalWrite(ledPin, HIGH);
    }
    else
    {
        digitalWrite(ledPin, LOW);
    }
    delay(200);
}