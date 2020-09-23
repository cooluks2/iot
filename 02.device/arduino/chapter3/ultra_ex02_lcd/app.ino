#include <MiniCom.h>
#include <Ultra.h>

#include <Led.h>

MiniCom com;
Ultra ultra(2, 3);
Led led(5);

void checkDistance() {
    int distance = ultra.read();
    com.print(0, "distance", distance);
    if(distance < 10) {
        led.on();
    } else {
        led.off();
    }
}

void setup() {
    com.init();
    com.setInterval(1000, checkDistance);
}

void loop() {
    com.run();
}