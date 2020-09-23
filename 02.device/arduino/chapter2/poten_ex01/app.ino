int vResister = A0;
void setup()
{
    Serial.begin(9600);
    pinMode(vResister, INPUT);
}
void loop()
{
    Serial.println(analogRead(vResister));
    delay(1000);
}