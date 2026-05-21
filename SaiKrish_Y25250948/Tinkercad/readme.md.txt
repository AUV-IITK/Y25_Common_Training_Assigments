const int lightThreshold = 800;
const float tempThreshold = 25.0; 
void setup() {
  pinMode(13,OUTPUT), pinMode(8,OUTPUT);
   Serial.begin(9600); 
}
void loop() {
  int light = analogRead(A0);
  if(light<lightThreshold){
    digitalWrite(13,HIGH);
  }else{
    digitalWrite(13,LOW);
  }
  int tempReading = analogRead(A3);
  float volt = tempReading*(5.0/1024.0);
  float temp = (volt-0.5)*100.0;
  Serial.print("LDR Value: ");
  Serial.print(light);
  Serial.print(" | Temperature Reading: ");
  Serial.println(temp);
  if(temp>tempThreshold){
    digitalWrite(8,HIGH); 
  }else{
    digitalWrite(8,LOW);
       }
  delay(100); 
}

logic: i have used photoresitor to detect brightness thereby deciding if to switch on led or not. We used temperature sensor to detect temperarure of the surrounding, we used npn transistor because otherwise the Arduino might blow off because of excessive current in digital pin. 