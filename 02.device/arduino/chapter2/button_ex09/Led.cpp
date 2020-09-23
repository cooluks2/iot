#include "Led.h"


Led::Led(int pin) : pin(pin){
    pinMode(pin, OUTPUT);
}

void Led::on(){
    digitalWrite(pin, HIGH);
}

void Led::off(){
    digitalWrite(pin, LOW);
}

void Led::toggle(){
    int state = digitalRead(pin);
    digitalWrite(pin, !state);
}

void Led::set(int value){
    digitalWrite(pin, value);
}