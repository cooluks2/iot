#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);
void setup()
{
    Serial.begin(9600);
    lcd.init();
    lcd.setCursor(0, 0);
    lcd.print("Arduino LCD");
    delay(1000);
    lcd.setCursor(0, 1);
    lcd.print("Welcome");
    delay(250);

    // LCD 백라이트 두번 점멸
    lcd.noBacklight();
    delay(250);
    lcd.backlight();
    delay(250);
    lcd.noBacklight();
    delay(250);
    lcd.backlight();
    delay(3000);
    // Open Serial Monitor Type to display 표시
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Open Serial Mntr");
    lcd.setCursor(0, 1);
    lcd.print("Type to display");
}


// 파이썬의 input() 함수에 해당..
String readLine() {
    //
    String line = "";
    // serial로 부터 한줄 입력 받아... line 변수에 저장

    while (Serial.available() > 0)
        {
            char ch = Serial.read();  // 문자 1개 리드
            if(ch != '\r' && ch != '\n')
                line += ch;
        }

    return line;
}


// 16x2
// 라인별로 한줄 전체를 덮어쓰는 형태...
void loop() {

    if (Serial.available()) // 수신된 데이터 있는지
    {
        delay(100);
        // lcd.clear(); // 긴 문장 보내고 ---> 짧은 문장 전송.
        lcd.setCursor(0, 0);
        lcd.print("Message from PC");
        lcd.setCursor(0, 1);
        
        String line = readLine();
        if(line != "") {  //수신데이터 유무
            lcd.setCursor(0, 1);
            char buf[17];  // null 문자열이 자동적으로 맨 끝에 자동으로 생겨서 17개로 배열만든다.
            float d = 3.14159;
            char buf2[10];
            dtostrf(d, 5, 3, buf2);

            // lcd.print(line.c_str());  // const char * 타입
            sprintf(buf,  "%-8s %s   ", line.c_str(), buf2);  // 문자열 buf에 출력, %-16s : 16칸 왼쪽 정렬
            lcd.print(buf);
        }
    }
}