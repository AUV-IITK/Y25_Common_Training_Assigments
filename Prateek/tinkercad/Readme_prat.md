# **CODE :**

const int lightThreshold = 400;

const float tempThreshold = 25.0;

void setup() {

&#x20; pinMode(13,OUTPUT), pinMode(9,OUTPUT);

&#x20;  Serial.begin(9600);

}

void loop() {

&#x20; int ldrValue = analogRead(A0);

&#x20; if(ldrValue<lightThreshold){

&#x20;   digitalWrite(13,HIGH);

&#x20; }else{

&#x20;   digitalWrite(13,LOW);

&#x20; }

&#x20; /////////////////

&#x20; int tempReading = analogRead(A1);

&#x20; // logic to convert analog reading to celsius

&#x20; float voltage = tempReading\*(5.0/1024.0);

&#x20; float temp = (voltage-0.5)\*100.0;

&#x20; Serial.print("LDR Value: ");

&#x20; Serial.print(ldrValue);

&#x20; Serial.print(" | Temperature Reading: ");

&#x20; Serial.println(temp);

&#x20; if(temp>tempThreshold){

&#x20;   digitalWrite(9,HIGH);

&#x20; }else{

&#x20;   digitalWrite(9,LOW);

&#x20;      }

&#x20; delay(100);

}



### &#x20;  **LOGIC EXPLANATION :**

In the circuit I used a LED to simulate turning on of light and a dc motor for fan. I used LDR and temperature sensor to detect brightness and temperature of the room. If the brightness is below a threshold value LED glows and if the temperature is greater than a specific threshold value the motor starts. I used a transistor as a switch to control the motor because if we use the Arduino pin to power the motor could damage it so transistor is used like a switch allowing flow of current from power rails to motor and taking that current from negative terminal of motor to collector and back to ground through emitter.

