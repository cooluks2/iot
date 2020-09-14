#define C 262
#define D 294
#define E 330
#define _F 349
#define G 392
#define A 440
#define B 494
#define H 523
int pzoPin = 5;
int tempo = 200; // 음 재생 시간 설정
int notes[25] = {
    G, G, A, A, G, G, E, G, G, E, E, D, G, G, A, A, G, G, E, G, E, D, E, C};
void setup()
{
    pinMode(pzoPin, OUTPUT);
}
void loop()
{
    for (int i = 0; i < 12; i++)
    {
        tone(pzoPin, notes[i], tempo);
        delay(300);
    }
    delay(100);
    for (int i = 12; i < 25; i++)
    {
        tone(pzoPin, notes[i], tempo);
        delay(300);
    }
}