#include <LiquidCrystal_I2C.h>
#include <SimpleTimer.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);
SimpleTimer timer;


void printTime() {
    char buf[17];
    unsigned long t = millis();

    //milisecond -> 시:분:초로 변환해서 출력
    int misec = t%1000/100; //100ms 단위
    t = t/1000; // 밀리초 -> 초
    int h = t / 3600; // 초 -> 시간
    int m = (t - (h*3600)) / 60; //초 -> 분
    int s = t - ( h*3600 + m*60); //초

    sprintf(buf, "%02d:%02d:%02d.%d", h, m, s, misec);

    lcd.setCursor(0,0);
    lcd.print(buf);
}

void setup()
{
    Serial.begin(9600);
    lcd.init();
    lcd.backlight();

    timer.setInterval(100, printTime);
}

void loop() {
    timer.run();
}