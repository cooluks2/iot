#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);
uint8_t smile1[8] = {0x00, 0x11, 0x00, 0x00, 0x00, 0x11, 0x0E, 0x00}; 
uint8_t smile2[8] = {0x00, 0x11, 0x00, 0x00, 0x00, 0x0E, 0x11, 0x00}; 
void setup()
{
    lcd.init();

    lcd.backlight();

    lcd.createChar(0, smile1);
    lcd.createChar(1, smile2);

    lcd.home();
    lcd.write(0);
    lcd.write(1);
}
void loop()
{
}