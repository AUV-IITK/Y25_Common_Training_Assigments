int tempPin = A0;
int ldrPin = A1;

int ledLight = 9;
int ledFan = 10;

void setup() {
  pinMode(ledLight, OUTPUT);
  pinMode(ledFan, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int tempValue = analogRead(tempPin);
  float voltage = tempValue * (5.0 / 1023.0);
  float temperature = (voltage - 0.5) * 100;

  int lightValue = analogRead(ldrPin);

  Serial.print("Temp: ");
  Serial.println(temperature);
  Serial.print("Light: ");
  Serial.println(lightValue);

  // Light condition
  if (lightValue < 500) {
    digitalWrite(ledLight, HIGH);
  } else {
    digitalWrite(ledLight, LOW);
  }

  // Temperature condition
  if (temperature > 30) {
    digitalWrite(ledFan, HIGH);
  } else {
    digitalWrite(ledFan, LOW);
  }

  delay(500);
}

<!-- The program continuously reads data from two sensors: a temperature sensor (TMP36) connected to pin A0 and a light sensor (LDR) connected to pin A1.

First, the analog value from the temperature sensor is converted into voltage, and then into temperature in degrees Celsius using the sensor’s formula. This allows the system to interpret real-world temperature values instead of raw readings.

At the same time, the LDR provides a value representing light intensity. Lower values correspond to darker surroundings, while higher values indicate brighter conditions.

Based on these inputs, the system applies simple conditional logic:

If the light intensity is below a chosen threshold, it means the surroundings are dark, so the light (LED connected to pin 9) is turned ON. Otherwise, it remains OFF.
If the temperature exceeds 30°C, the fan (LED connected to pin 10) is turned ON. Otherwise, it remains OFF.

Both conditions are evaluated independently inside the loop, which runs continuously. This ensures that the system can respond in real time to changes in both temperature and light without one affecting the other.

Overall, the program demonstrates how sensor inputs can be processed and used to control outputs automatically, forming a basic smart room control system. -->