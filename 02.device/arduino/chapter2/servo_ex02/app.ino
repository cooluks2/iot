#include "AnalogSensor.h"
#include <Servo.h>
#include <LiquidCrystal_I2C.h>

AnalogSensor poten(A0, 0, 180);
LiquidCrystal_I2C lcd(0x27, 16, 2);
Servo servoMotor;

const int servoPin = 9;

void setup()
{   
    lcd.init();
    lcd.backlight();
    lcd.clear();

    servoMotor.attach(servoPin);
    servoMotor.write(poten.read());
    
    Serial.begin(9600);
}
void loop()
{   
    char buf[17];

    int angle = poten.read();
    servoMotor.write(angle);

    sprintf(buf, "angle : %3d", angle);
    lcd.setCursor(0, 0);
    lcd.print(buf);
}