#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

const int ledPin = 3;
const int potentiometerPin = A0;
int potentiometerValue;
int brightness;

void setup() {
    lcd.init();
    lcd.backlight();
    lcd.clear();
    Serial.begin(9600);
}

void loop() {
    char buf[17];

    potentiometerValue = analogRead(potentiometerPin);  // 0 ~ 1023

    sprintf(buf, "org : %4d", potentiometerValue);
    lcd.setCursor(0, 0);
    lcd.print(buf);

    brightness = map(potentiometerValue, 0, 1023, 180, 0); // 밝기 단계 확인 후
    // brightness = map(potentiometerValue, 0, 1023, 0, 255);

    sprintf(buf, "bright : %4d", brightness);
    lcd.setCursor(0, 1);
    lcd.print(buf);

    analogWrite(ledPin, brightness);
}