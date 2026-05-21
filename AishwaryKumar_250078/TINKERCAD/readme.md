Link to TinkerCAD :- https://www.tinkercad.com/things/5b7o8P80uu2-temp-and-light-sensor?sharecode=9pRBgjKO_oX5oUuNo-CrwuwxPxYEENGeQYZu71zIKtA

void setup() {
pinMode(A0, INPUT); 
pinMode(A5, INPUT);
pinMode(7, OUTPUT);
pinMode(4, OUTPUT);
Serial.begin(9600);
}

void loop() {
int tempVal = analogRead(A0);
float voltage = (tempVal / 1024.0) * 5.0;
float celsius = (voltage - 0.5) * 100;
int lightVal = analogRead(A5);
if (celsius < 25) {
digitalWrite(7, LOW);
}
  
  else{
digitalWrite(7, HIGH);
}
if (lightVal > 950) {
digitalWrite(4, LOW);
} 
  else {
  digitalWrite(4, HIGH);
  }
delay(500); 
}

Logic :- 
I have used TMP36 for temperature senor and PhotoTransistor for LDR
  Temp Sensor :- 
   1) It is being given a analog input which is converted to voltage.
   2) For converting to voltage the value read from analog is being divided by 1024 since input voltage is mapped between 0-1023 and then being multiplied by 5 since there is 5V voltage
   3)Then it is being converted to celsius 
   4)TMP36 has a offset value of 0.5 so I am subracting that and then multiplying by 100 for scaling
 Light Sensor :-
    1) The emitter is connected to GND and analog input and the collector is connected to power.
    2) The code checks if the reading is above a specific value for turning on and off the led.
    3) I have obtained the thresold value through hit and trial using Serial Monitor.
   
