#include "Led.h"
#include "Button.h"

Led led(4);
Button btn(11);

void setup() {
    Serial.begin(9600);
}

void work() {
    led.toggle();
}

void loop()
{
    led.set(btn.read());
}