#include "joystick.h"

JoyStick::JoyStick(int x, int y, int z)
    : jX(x), jY(y), btn(z) {

}

int JoyStick::readX() {
    return jX.read();
}

int JoyStick::readY() {
    return jY.read();
}

void JoyStick::setRangeX(int toMin, int toMax) {
    jX.setRange(toMin, toMax);
}

void JoyStick::setRangeY(int toMin, int toMax) {
    jY.setRange(toMin, toMax);
}

int JoyStick::readZ() {
    return btn.read();
}

void JoyStick::setCallback(button_callback_t callback) {
    btn.setCallback(callback);
}

void JoyStick::check() {
    btn.check();
}

joystick_value_t JoyStick::read() {
    joystick_value_t value;
    value.x = readX();
    value.y = readY();
    value.z = readZ();
    return value;
}