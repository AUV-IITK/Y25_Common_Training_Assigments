// Pins
const int ldrPin = A5;
const int tempPin = A4;

const int bulbPin = 9;   // Large bulb
const int fanPin  = 8;   // Small LED replacing fan

// Thresholds
const int lightThreshold = 900;
const float tempThreshold = 30.0; // in degree Celsius

void setup() {
  pinMode(bulbPin, OUTPUT);
  pinMode(fanPin, OUTPUT);

  Serial.begin(9600);
}

void loop() {


  int lightValue = analogRead(ldrPin);

  // Dim light -> turn bulb ON
  if (lightValue < lightThreshold) {
    digitalWrite(bulbPin, HIGH);
  } else {
    digitalWrite(bulbPin, LOW);
  }

  int tempReading = analogRead(tempPin);

  // TMP36 conversion
  float voltage = tempReading * (5.0 / 1023.0);
  float temperatureC = (voltage - 0.5) * 100.0;


  if (temperatureC > tempThreshold) {
    digitalWrite(fanPin, HIGH);
  } else {
    digitalWrite(fanPin, LOW);
  }

  // Serial Monitor output
  Serial.print("Light Value: ");
  Serial.print(lightValue);

  Serial.print("   Temperature: ");
  Serial.println(temperatureC);

  delay(500);
}