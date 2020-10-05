#include "BtMiniCom.h"
#include <Led.h>

void received(String msg);

Led led(13);
BtMiniCom com(2, 3, received);

void received(String msg) {
    if(msg=="on") {
        led.on();
        com.send("OK");
    } else if(msg=="off") {
        led.off();
        com.send("OK");
    } else {
        com.send("Bad Command");
    }
}

void setup(){
    com.init();
}

void loop() {
   com.run();
}

