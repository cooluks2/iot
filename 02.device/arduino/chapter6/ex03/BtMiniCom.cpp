#include "BtMiniCom.h"

BtMiniCom::BtMiniCom(int rx, int tx,  btminicom_callback_t callback) 
    : MiniCom(), btSerial(rx, tx), callback(callback) {
}

void BtMiniCom::init() {
    MiniCom::init();
    btSerial.begin(9600);
}

String BtMiniCom::readLine() {  // \r\n를 제외한 문자열을 리턴
    String message = "";
    while(btSerial.available()) {
        char data = (char)btSerial.read();
        if(data == '\r') continue;
        if(data == '\n') break;

        message += data;
        delay(5);  // 수신 문자열 끊김 방지
    }
    return message;
}

void BtMiniCom::send(const char *msg) {
    btSerial.println(msg);
}


void BtMiniCom::run() {
    String msg = readLine();
    if(msg != "" && callback != NULL) {
        callback(msg);
    }
    MiniCom::run();
}
