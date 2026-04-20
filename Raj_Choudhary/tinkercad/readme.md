
// ANALOG PINS : defining 
const int ldrPin = A0;
const int tempPin = A1;

// Digiatl pins : defining for the output 
const int lightLED = 7;
const int fanLED = 8;

// Steup for making connecting the outputs to the sensors 
void setup() {
  pinMode(lightLED, OUTPUT);
  pinMode(fanLED, OUTPUT);
  Serial.begin(9600);
}

void loop() {

  int ldrValue = analogRead(ldrPin);


  int tempValue = analogRead(tempPin);
  float voltage = tempValue * (5.0 / 1023.0);
  float temperature = (voltage - 0.5) * 100;
  
  Serial.print("LDR: ");
  Serial.print(ldrValue);
  Serial.print(" | Temp: ");
  Serial.println(temperature);

 // LOGICAL PART OF THE CIRCUIT CODE 
  if (ldrValue < 300) {
    digitalWrite(lightLED, HIGH);
  } else {
    digitalWrite(lightLED, LOW);
  }


  if (temperature > 30) {
    digitalWrite(fanLED, HIGH);
  } else {
    digitalWrite(fanLED, LOW);
  }

  delay(500);
}


Logic Explainations :

1. The circuit is based on real life problem that we have to build a system able to automatically sense the changes in the light and temperature of a room and then based on the sensing it can switch on off the fan and the lights of the system .

2. for making the circuit i used the LDR (uses the light and then changes the resistance accordingly for changing the current flowing ) and temperature sensor ( Snese the temperature and give the volatage accordingly )

3. The most logial part of the system is to make the if - else condition for the system . Both the sensor gives the analog outputs and code convert it to digital using the conditions .Code actually states that if the output temperature is more then a paricular value then the fan will move otherwise not ,same in case of the light if the brightness is lesser then a particular value then the code will turn on the lights .

4. Testing : In the serial monitor the reading of the temperature and light brightness are showing , we can change both using the slider on the sensors and check the change in leds at differnt values and also in serail monitor .