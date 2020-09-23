#include "AnalogSensor.h"

AnalogSensor::AnalogSensor(int pin, int toMin, int toMax)
    : pin(pin), toMin(toMin), toMax(toMax) {

}

void AnalogSensor::setRange(int toMin, int toMax) {
    this->toMin = toMin;
    this->toMax = toMax;
}

int AnalogSensor::read() {
    int value = analogRead(pin);
    return map(value, 0, 1023, toMin, toMax);
}