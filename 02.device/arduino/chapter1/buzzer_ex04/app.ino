int speakerPin = 5;
int melody[] = {262, 294, 330, 349, 392, 440, 494, 523};
void setup()
{
    pinMode(speakerPin, OUTPUT);
}
void loop()
{
    // 도파도솔
    tone(speakerPin, melody[0], 230);
    delay(250);
    tone(speakerPin, melody[3], 230);
    delay(250);
    tone(speakerPin, melody[0], 230);
    delay(250);
    tone(speakerPin, melody[4], 230);
    delay(250);
    delay(2000);
}