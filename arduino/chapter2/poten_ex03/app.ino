const int ledPin = 3;
const int potentiometerPin = A0;
int potentiometerValue;
int brightness;
void setup()
{
    Serial.begin(9600);
}
void loop()
{
    potentiometerValue = analogRead(potentiometerPin);
    Serial.print("potentiometer Value : ");
    Serial.println(potentiometerValue);
    brightness = map(potentiometerValue, 0, 1023, 0, 255);
    Serial.print("potentiometer Value : ");
    Serial.println(brightness);
    analogWrite(ledPin, brightness);
}