#include <pitches.h>
int speakerPin = 5;
int melody[] = {
    NOTE_C4, NOTE_G3, NOTE_G3, NOTE_A3, NOTE_G3, 0, NOTE_B3, NOTE_C4,
};
// 음표의 길이 4 = 4분음표(한박자), 8 = 8분 음표(반 박자)
int noteDurations[] = {4, 8, 8, 4, 4, 4, 4, 4};
void setup()
{
    for (int thisNote = 0; thisNote < 8; thisNote++)
    {
        int noteDuration = 1000 / noteDurations[thisNote];
        tone(speakerPin, melody[thisNote], noteDuration);
        // 음을 구별하기 위해 그 사이에 최소한의 간격을 둔다.
        int pauseBetweenNotes = noteDuration * 1.30;
        delay(pauseBetweenNotes);
        noTone(speakerPin); // 멜로디 멈춤
    }
}
void loop() {}