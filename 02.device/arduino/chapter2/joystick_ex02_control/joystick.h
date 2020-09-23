#pragma once

#include <Arduino.h>
#include <AnalogSensor.h>
#include <Button.h>

typedef struct {  // 기본적으로 public
    int x;
    int y;
    int z;
} joystick_value_t;

class JoyStick {
protected:  // 상속..    private : 상속이 안된다. ☆☆☆☆☆
    AnalogSensor jX;
    AnalogSensor jY;
    Button btn;

public:
    JoyStick(int x, int y, int z);

    int readX();
    int readY();
    void setRangeX(int toMin, int toMax);
    void setRangeY(int toMin, int toMax);

    int readZ();  // 버튼의 상태 읽는 것
    void setCallback(button_callback_t callback);
    void check();

    joystick_value_t read();  // 파이썬에서는 리스트, 튜플
};