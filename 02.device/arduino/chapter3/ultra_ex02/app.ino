#include <MiniCom.h>
#include <Servo.h>
#include <Ultra.h>
#include "Pulse.h"
#include <Led.h>

MiniCom com;
Ultra ultra(2, 3);
Led led(5);
Servo servo;
Pulse pulse(100, 500);

// 5단계로 운용
int delaytimes[] = {
    50, 100, 200, 500, 1000
};

void pulseCallback(int value) {
    
    // LED 제어
    led.set(value);
}

void checkDistance() {
    int distance = ultra.read();
    com.print(0, "distance", distance);
    if(distance < 10) {
        // led.on();
        // Pulse의 offDelay를 distance를 고려하여 조정
        int offDelay = map(distance, 0, 9, 0, 4);
        pulse.setDelay(10, delaytimes[offDelay]);

        servo.write(90);
        if(!pulse.getState()) {  // 처음 10cm 이하로 됐을 때
            pulse.play();
        }
    } else {
        if(pulse.getState()) {
            pulse.stop();
        }
        // led.off();
        servo.write(0);
    }
}

void setup() {
    com.init();
    servo.attach(9);
    servo.write(0);
    pulse.setCallback(pulseCallback);
    com.setInterval(1000, checkDistance);
}

void loop() {
    com.run();
    pulse.run();
}

// Event driven 방식...