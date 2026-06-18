In the circuit I used analogue input and output.
In code for fan I used condition -
  - OFF (temperature <20)
  - Linear increase from lowest to highest intensity possible (20 < temperature < 40) 
  - ON in full intensity (temperature > 40)

And for brightness I used linear increase in all over the range because of absence of any useful measure like Celsius scale in previous one

-------code--------


// C++ code
//

int t_40=184, t_20=141;
int diff=t_40-t_20;
  
  
void setup()
{
  pinMode(13, OUTPUT);
  pinMode(8, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  
  int temp_val=analogRead(A0);
 // Serial.println(temp_val);
  if(temp_val>t_20&&temp_val<t_40){
   analogWrite(11,(long)(temp_val-t_20)*255/diff);
  }
  else if(temp_val<t_20){
  	analogWrite(11,0);
  }
  else{
  	analogWrite(11,255);
  }
  int brightness=analogRead(A5);
  Serial.println(brightness);
  analogWrite(10, (long)((255.0/673.0)*(679-brightness)));
}
