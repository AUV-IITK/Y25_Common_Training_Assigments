// C++ code
//
//Please view in the Code section
int animationSpeed = 400;

int sensorPin_1 = A0;  #for fan
int sensorPin_2 = A1;  #for light
int ledPin_1 = 13;     #for fan
int ledPin_2= 11;      #for light

void setup() {
  pinMode(ledPin_1, OUTPUT);
  pinMode(ledPin_2, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int temp_data = analogRead(sensorPin_1);
  
  //FAN

  // Convert to voltage
  float voltage = temp_data * (5.0 / 1023.0); 
  // we need to convert  as per our voltage of 5V to get appropriate readings since the analog outputs a number between 0-1023(10-bit)

  // Convert to temperature 
  float temperature = (voltage-0.5) * 100;
  //this is to scale the voltage range as per our convenience of setting the temperature threshold
  //-0.5 is used since the available temperature sensor was TMP36 and this value can differ

  Serial.println(temperature);
  //to output the temperature on Serial Monitor

  if (temperature > 32) {  // threshold
    digitalWrite(ledPin_1, HIGH);
    delay(animationSpeed);
  } else {
    digitalWrite(ledPin_1, LOW);
    delay(animationSpeed);
  }
  
  //LIGHT
  
  int light_data= analogRead(sensorPin_2);
  
  Serial.println(light_data);
  
  if(light_data<938){
    digitalWrite(ledPin_2, HIGH);
    delay(animationSpeed);
  } else {
    digitalWrite(ledPin_2, LOW);
    delay(animationSpeed);
  }
  

  
}
