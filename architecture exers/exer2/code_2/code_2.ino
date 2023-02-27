#include <LiquidCrystal.h>
LiquidCrystal lcd(2,3,4,5,6,7);
int tempC;
int tempF;

int i = 0;
int counter = 0;

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);
  pinMode(A0, INPUT); //temp
  pinMode(A1, INPUT); // air
  pinMode(A2, INPUT); // water
  pinMode(A3, INPUT); // anemometer
  pinMode(A4, INPUT); // humidity

  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);

}

void lcdPrint(String text, int value){
  lcd.clear();
  lcd.setCursor(0, 0); 
  lcd.print(text);
  lcd.setCursor(0, 1); 
  lcd.print(value);  
}

void loop() {
  if(i<1){
    digitalWrite(11,HIGH);
    digitalWrite(12,LOW);
    i=1;
  }else{
    digitalWrite(11,LOW);
    digitalWrite(12,HIGH);
    i=0;
  }
  counter++;
  delay(200);


  int temperature = analogRead(A0);
  int air = analogRead(A1);
  int waterLevel = analogRead(A2);
  int anemometer = analogRead(A3);
  int humid = analogRead(A4);
  
  bool windSpeed_btn = digitalRead(8) && digitalRead(11);
  bool humid_btn = digitalRead(9) && digitalRead(11);
  bool tempC_btn = digitalRead(10) && digitalRead(11);

  bool waterlvl_btn = digitalRead(8) && digitalRead(12);
  bool air_btn = digitalRead(9) && digitalRead(12);
  bool tempF_btn = digitalRead(10) && digitalRead(12);


  //CONVERSION
  float voltage = temperature * 5.0;
  tempC = (((voltage - 0.5) * 100+50)/1000)-2;
  tempF = (tempC * (9/5)) + 32;
  air += 114;
  humid += 541;
  anemometer += 636;
  

  if(windSpeed_btn){
    lcdPrint("Wind Speed km/h:", anemometer);
  }
  if(humid_btn){
    lcdPrint("Humidity:", humid);
  }
  if(tempC_btn){
    lcdPrint("Temp C:", tempC);
  }

  if(waterlvl_btn){
    lcdPrint("Water Level:", waterLevel);
  }
  if(air_btn){
    lcdPrint("Air Pressure:", air);
  }
  if(tempF_btn){
    lcdPrint("Temp F:", tempF);
  }

  Serial.print(anemometer);
  Serial.print(",");
  Serial.print(air);
  Serial.print(",");
  Serial.print(waterLevel);
  Serial.print(",");
  Serial.print(humid);
  Serial.print(",");
  Serial.print(tempC);
  Serial.print(",");
  Serial.println(tempF);
  
  delay(1000);
  
}

