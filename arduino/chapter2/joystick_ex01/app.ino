#include <AnalogSensor.h>
#include <LiquidCrystal_I2C.h>
#include <SimpleTimer.h>
#include <Button.h>

AnalogSensor jX(A0, 0, 1023);
AnalogSensor jY(A1, 0, 1023);
Button btn(2);


LiquidCrystal_I2C lcd(0x27, 16, 2);
SimpleTimer timer;

void readJoystick() {
    char buf[17];

    int x = jX.read();
    int y = jY.read();
    int z = btn.read();
    sprintf(buf, "x: %4d, y: %4d", x, y);
    lcd.setCursor(0, 0);
    lcd.print(buf);

    sprintf(buf, "z: %4d", z);
    lcd.setCursor(0, 1);
    lcd.print(buf);
}

void setup() {
    lcd.init();
    lcd.backlight();
    lcd.clear();

    timer.setInterval(50, readJoystick);
    Serial.begin(9600);
}

void loop() {
    timer.run();
}