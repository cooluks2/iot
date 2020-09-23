#include <MiniCom.h>
#include "Ultra.h"

MiniCom com;
Ultra ultra(2, 3);

void checkDistance() {
    int distance = ultra.read();
    com.print(0, "distance", distance);
}

void setup() {
    com.init();
    com.setInterval(1000, checkDistance);
}

void loop() {
    com.run();
}