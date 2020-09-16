int echoPin = 2;
int triggerPin = 3;
int spearkerPin = 5;
void setup()
{
    Serial.begin(9600);
    pinMode(echoPin, INPUT);
    pinMode(triggerPin, OUTPUT);
    pinMode(spearkerPin, OUTPUT);
}

void loop()
{
    float duration;
    digitalWrite(triggerPin, HIGH);
    delay(10);
    digitalWrite(triggerPin, LOW);
    int distance = pulseIn(echoPin, HIGH) / 58;
    noTone(spearkerPin);
    Serial.println(distance);
    if (distance < 60 && distance >= 40)
    {
        tone(spearkerPin, 1000, 300);
        delay(1000);
    }
    else if (distance < 30 && distance >= 20)
    {
        tone(spearkerPin, 1000, 200);
        delay(500);
    }
    else if (distance < 20 && distance >= 10)
    {
        tone(spearkerPin, 1000, 100);
        delay(200);
    }
    else if (distance < 10)
    {
        tone(spearkerPin, 1000, 50);
        delay(70);
    }
}