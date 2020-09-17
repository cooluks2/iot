#include <MiniCom.h>
#include <Servo.h>
#include <Ultra.h>

#include <Led.h>

MiniCom com;
Ultra ultra(2, 3);
Led led(5);
Servo servo;

void checkDistance() {
    int distance = ultra.read();
    com.print(0, "distance", distance);
    if(distance < 10) {
        led.on();
        servo.write(90);
    } else {
        led.off();
        servo.write(0);
    }
}

void setup() {
    com.init();
    servo.attach(9);
    servo.write(0);
    com.setInterval(1000, checkDistance);
}

void loop() {
    com.run();
}