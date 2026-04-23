
int ldrPin = A0;
int tempPin = A1;

int lightLED = 7;
int fanLED = 8;

bool lightState = false;  

void setup() {
  pinMode(lightLED, OUTPUT);
  pinMode(fanLED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int ldrValue = analogRead(ldrPin);

  
  if (!lightState && ldrValue < 450) {
    lightState = true;
    digitalWrite(lightLED, HIGH);
  }
  else if (lightState && ldrValue > 550) {
    lightState = false;
    digitalWrite(lightLED, LOW);
  }

  
  int tempValue = analogRead(tempPin);
  float voltage = tempValue * (5.0 / 1023.0);
  float temperature = (voltage - 0.5) * 100;

  
  if (temperature > 30) {
    digitalWrite(fanLED, HIGH);
  } else {
    digitalWrite(fanLED, LOW);
  }

  delay(500);
}
