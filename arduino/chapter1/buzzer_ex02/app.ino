int speakerPin = 5;
void setup()
{
}
void loop()
{
    tone(speakerPin, 5000, 1000); // 비동기 함수
    delay(2000); // 1초 동안 소리, 1초 동안 소리X
}