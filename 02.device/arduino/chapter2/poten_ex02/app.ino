int LED = 3;
void setup()
{
    pinMode(LED, OUTPUT);
}
void loop()
{
    int readVal = analogRead(A0);
    int brightVal = readVal / 4;  //PWM의 범위는 0~255
    analogWrite(LED, brightVal);
    delay(10);
}