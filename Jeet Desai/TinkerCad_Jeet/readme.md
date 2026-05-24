const int tempPin = A0;    
const int ldrPin  = A1;    
const int lightLED = 13;     
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

// logic - threshold values of sensors have been defined above which upon getting crossed, the if else loop will turn on/off the respective LED depending on the requirement
