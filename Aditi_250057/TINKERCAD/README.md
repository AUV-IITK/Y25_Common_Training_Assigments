<img width="936" height="796" alt="image" src="https://github.com/user-attachments/assets/5b5246be-bcb1-4a4c-97e5-8b7a780853c5" />





<img width="543" height="696" alt="image" src="https://github.com/user-attachments/assets/a903ca3c-1287-4d70-8949-4f66944355ec" />



**CODE :**
// Pin Definitions
const int LDR_PIN = A0;      
const int TMP_PIN = A1;      
const int LIGHT_LED = 8;     
const int FAN_LED = 9;       

// Thresholds 
const int LIGHT_THRESHOLD = 500; 
const float TEMP_THRESHOLD = 30.0; 
void setup() {
  pinMode(LIGHT_LED, OUTPUT);
  pinMode(FAN_LED, OUTPUT);
  Serial.begin(9600); 
}

void loop() {
 
  int lightValue = analogRead(LDR_PIN);
  
  if (lightValue < LIGHT_THRESHOLD) {
    digitalWrite(LIGHT_LED, HIGH); 
  } else {
    digitalWrite(LIGHT_LED, LOW);
  }

 
  int tempRaw = analogRead(TMP_PIN);
 
  float voltage = tempRaw * (5.0 / 1024.0);
  float tempC = (voltage - 0.5) * 100;

  if (tempC > TEMP_THRESHOLD) {
    digitalWrite(FAN_LED, HIGH); 
  } else {
    digitalWrite(FAN_LED, LOW);
  }

  Serial.print("Light: "); Serial.print(lightValue);
  Serial.print(" | Temp: "); Serial.println(tempC);

  delay(100); 
}


**
LOGIC EXPLAINATION :**
This Arduino program continuously monitors light and temperature to control two outputs like a tiny automated room assistant. It reads the light intensity from an LDR on analog pin A0 and compares it with a threshold value of 500; if the reading is below this threshold, it assumes the environment is dark and turns ON the light LED on pin 8, otherwise it turns it OFF. At the same time, it reads the temperature sensor value from analog pin A1, converts the raw reading into voltage and then into temperature in Celsius using the sensor’s formula, and compares it with a threshold of 30°C. If the temperature exceeds this limit, it turns ON the fan LED on pin 9, otherwise it keeps it OFF. Throughout the process, it prints both light and temperature values to the serial monitor for observation and repeats this cycle every 100 milliseconds, ensuring real-time sensing and control.




