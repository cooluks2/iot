int pin_button = 11;
int led = 13;
boolean state_previous = true;
boolean state_current;
void setup()
{
    Serial.begin(9600);
    pinMode(pin_button, INPUT_PULLUP);
    pinMode(led, OUTPUT);
}

void work() {
    int ledState = digitalRead(led);
    digitalWrite(led, !ledState);
}

void loop()
{
    state_current = digitalRead(pin_button);
    if (!state_current) { // 누른 경우
        if (state_previous == true)
        {
            state_previous = false;
            // 버튼을 누른 시점에서 해야할 작업
            work();
        }
        delay(10);  // 추가!
    }
    else
    {
        state_previous = true;
    }
}