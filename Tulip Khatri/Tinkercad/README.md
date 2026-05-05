// Smart Room Controller 
const int ldrPin   = A1;
const int tmpPin   = A0;
const int ledLight = 10;
const int ledFan   = 11;

const int   darkThreshold = 400;
const float hotThreshold  = 30.0;

void setup() {
  pinMode(ledLight, OUTPUT);
  pinMode(ledFan,   OUTPUT);
  Serial.begin(9600);
  Serial.println("Smart Room Controller Started");
}

void loop() {
  int ldrValue = analogRead(ldrPin);

  int   tmpRaw  = analogRead(tmpPin);
  float voltage = tmpRaw * (5.0 / 1023.0);  
  float tempC   = (voltage - 0.5) * 100.0;

  
  if (tempC < -40.0 || tempC > 125.0) {
    Serial.println("TMP36 read error");
    delay(1000);
    return;
  }

  
  bool isDark = ldrValue < darkThreshold;
  bool isHot  = tempC > hotThreshold;

  digitalWrite(ledLight, isDark ? HIGH : LOW);
  digitalWrite(ledFan,   isHot  ? HIGH : LOW);

  
  Serial.print("LDR: ");
  Serial.print(ldrValue);
  Serial.print(isDark ? " [DARK]" : " [BRIGHT]");
  Serial.print(" | Temp: ");
  Serial.print(tempC, 1);        
  Serial.print(" C");
  Serial.println(isHot ? " [HOT]" : " [OK]");

  delay(500);   
}
