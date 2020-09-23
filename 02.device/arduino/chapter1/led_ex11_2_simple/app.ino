#include <SimpleTimer.h>

SimpleTimer timer;

void printTest1() {
    Serial.println("simple called by 1 sec");
}

void printTest2() {
    Serial.println("simple called by 0.5 sec");
}


void setup() {
    Serial.begin(9600);
    timer.setInterval(1000, printTest1);
    timer.setInterval(500, printTest2);
}

void loop() {
    timer.run();
}