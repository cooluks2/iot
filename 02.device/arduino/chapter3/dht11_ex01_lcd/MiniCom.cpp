#include "MiniCom.h"

MiniCom::MiniCom() : lcd(0x27, 16, 2) {

}

void MiniCom::init() {
    Serial.begin(9600);
    lcd.init();
    lcd.backlight();

}

int MiniCom::setInterval(unsigned long d, timer_callback f) {
    return timer.setInterval(d, f);
}

void MiniCom::run() {
    timer.run();
}

void MiniCom::print(int col, int row, const char *pMsg) {
    lcd.setCursor(col, row);
    char buf[17];
    sprintf(buf, "%-16s", pMsg);  // 이전의 긴 문장을 덮어쓰기 위해 -16s (clear 할 필요 없음)
    lcd.print(buf);
}

void MiniCom::print(int row, const char *pMsg) {
    print(0, row, pMsg);
}

void MiniCom::print(int row,const char *pTitle , int value) {
    char buf[17];
    sprintf(buf, "%s: %d", pTitle, value);
    print(0, row, buf);
}

void MiniCom::print(int row, const char *pTitle, double value, int width) {
    char buf[17];
    char temp[14];
    dtostrf(value, width, 2, temp);
    sprintf(buf, "%s: %s", pTitle, temp);
    print(0, row, buf);
}