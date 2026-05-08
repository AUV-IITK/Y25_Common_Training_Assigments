# Tinkercad Assignment
int threshold=950;

void setup() {
  pinMode(8, OUTPUT);   // LED 1 - Light
  pinMode(9, OUTPUT);   // LED 2 - Fan
}

void loop() {
  // Read LDR
  int ldr = analogRead(A0);       // Low value = dark
  if (ldr < threshold)
    digitalWrite(8, HIGH);             // Light ON
  else
    digitalWrite(8, LOW);              // Light OFF

  // Read Temperature
  float voltage = analogRead(A1) * (5.0 / 1023.0);
  float tempC = (voltage - 0.5) * 100; // TMP36 formula
  if (tempC > 24)
    digitalWrite(9, HIGH);             // Fan ON
  else
    digitalWrite(9, LOW);              // Fan OFF
}
<!-- the photoresistor is connected to a resistor and an arduino to the analog read A0 .the photoresistor will show a slider once we start simulation and this value is storedin ldr variable 
i have chosen a global variable threshold to depict the surrounding brightness level when the value of the slider will be < threshold means light need to be on and for that i have connected an led for "Light" to D8 and if ldr<threshold -> led glow else off . 
<!-- for fan i have used a TMP sensor and an analog input A1 and an led to reflect output while simulation we can control the temp with a slider so if temp >24 fan on else off.
