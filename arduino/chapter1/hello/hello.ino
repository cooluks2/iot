void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);             // 시리얼통신 시작(속도:9600)
  Serial.println("hello, Arduino"); // 시리얼모니터에 "hello, Arduino"를 출력
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("hello, Arduino");
  delay(500);  // 500ms 동안 대기...
}
