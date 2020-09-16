#include <LiquidCrystal_I2C.h>
#include <Led.h>
#include <AnalogSensor.h>
#include <PWMLed.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);
AnalogSensor illu(A0, 0, 100);

// Led led(3);
PWMLed led(3);

void setup() {
    Serial.begin(9600);
    lcd.init();
    lcd.backlight();
    led.off();   
}

void printIllu(int value) {
    char buf[17];
    sprintf(buf, "brightness : %3d", value);
    lcd.setCursor(0, 0);
    lcd.print(buf);
}

void loop() {
    int readVal = illu.read();
    int brightness = map(readVal, 0, 255, 255, 0);
    printIllu(readVal);
    led.set(brightness);
    // if(readVal < 20) {
    //     led.on();
    // } else {
    //     led.off();
    // }
    delay(200);
}