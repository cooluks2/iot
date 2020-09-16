#pragma once

#include <Arduino.h>
#include <LiquidCrystal_I2C.h>
#include <SimpleTimer.h>

class MiniCom {
protected:
    LiquidCrystal_I2C lcd;
    SimpleTimer timer;

public:
    MiniCom();    // 생성자
    void init();  // 초기화 코드
    // SimpleTimer.h 의 setInterval 매개변수
    int setInterval(unsigned long d, timer_callback f);  // 타이머 콜백 등록
    void run();   // 타이머 운영 및 기타 처리

    // LCD 출력 지원 함수(helper 함수)
    void print(int col, int row, const char *pMsg);
    void print(int row, const char *pMsg);  // 정해진 행에 메시지 출력
    void print(int row, const char *pTitle ,int value);
    void print(int row, const char *pTitle, double value, int width=6);
};

// 위 두 함수 역할
// title: int value
// title: double value