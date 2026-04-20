const int tempPin = A0;    
const int ldrPin  = A1;    
const int lightLED = 12;     
const int fanLED   = 11;    
const int ldrThreshold = 200;  
const float tempThreshold = 30.0;
void setup()
{
  pinMode(lightLED, OUTPUT);
  pinMode(fanLED, OUTPUT);
}
void loop()
{
  int ldrValue = analogRead(ldrPin);
  if (ldrValue < ldrThreshold)
    digitalWrite(lightLED, HIGH);
  else
    digitalWrite(lightLED, LOW);
  int tempValue = analogRead(tempPin);
  float voltage = tempValue * (5.0 / 1023.0);
  float temperature = (voltage - 0.5) * 100.0;
  if (temperature > tempThreshold)
    digitalWrite(fanLED, HIGH);
  else
    digitalWrite(fanLED, LOW);
  delay(500);
}

LOGIC
A0 and A1 are temperature sensor and light sensor input resepectively
12 contrls light and 11 controls fan
choose thresholds for both variables
if ldr value is below threshold then it will turn on
convert raw sensor value into volts and then convert that to temperature value
use the threshold condition again





