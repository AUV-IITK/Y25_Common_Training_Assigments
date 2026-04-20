# Smart Room Controller

## Objective
This project controls a room light and fan automatically using sensors.

## Components Used
- Arduino Uno
- TMP36 Temperature Sensor
- LDR
- 2 LEDs
- Resistors
- Breadboard

## Working Logic
- If the room becomes dark, the LDR detects low light and LED 1 turns ON (Light).
- If the temperature rises above 30°C, the temperature sensor activates LED 2 (Fan).
- Both systems work independently and continuously.

## Output
- LED 1 = Room Light
- LED 2 = Fan

## Code

```cpp
int tempPin = A0;
int ldrPin = A1;

int lightLED = 8;   // Yellow
int fanLED = 9;     // Red

void setup() {
  pinMode(lightLED, OUTPUT);
  pinMode(fanLED, OUTPUT);
  Serial.begin(9600);
}

void loop() {

  // ----- Light Sensor -----
  int lightValue = analogRead(ldrPin);
  Serial.print("LDR: ");
  Serial.println(lightValue);

  if (lightValue < 500) {
    digitalWrite(lightLED, HIGH);   // Dark
  } else {
    digitalWrite(lightLED, LOW);    // Bright
  }

  // ----- Temperature Sensor -----
  int sensorValue = analogRead(tempPin);
  float voltage = sensorValue * (5.0 / 1023.0);
  float temperature = (voltage - 0.5) * 100;

  if (temperature > 30) {
    digitalWrite(fanLED, HIGH);
  } else {
    digitalWrite(fanLED, LOW);
  }

  delay(300);
}
