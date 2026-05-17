# Smart Room Controller

## Code

```cpp
int ldrPin = A0;
int tempPin = A1;

int lightLED = 7;
int fanLED = 8;

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

  
  if (ldrValue < 500) {  
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
```

---

## Logic Explanation

* LDR detects brightness using analog values. (connected to A0 pin)
* If value is low (less than 500) that means environment is dark which implies Light turns ON.
* Temperature sensor gives voltage proportional to temperature. (connected to A1 pin)
* If temperature is less than 30°C then Fan turns ON.
* Both systems run continuously and independently.
