int speakerPin = 5;
int melody[] = {262, 294, 330, 349, 392, 440, 494, 523};
void setup()
{
    for (int i = 0; i < 8; i++)
    {
        tone(speakerPin, melody[i], 250);
        delay(400);
        noTone(speakerPin);
    }
}
void loop()
{
}