//CO2

#include <Wire.h>
#include <NDIR_I2C.h>
#include "DHT.h"
#define DHTPIN 16 
#define DHTTYPE DHT22  
NDIR_I2C mySensor(0x4D); //Adaptor's I2C address (7-bit, default: 0x4D)

//Humidity and temperature
DHT dht(DHTPIN, DHTTYPE);

//Sound
int soundPin = 0;      //To pin A0 on sound module
int thresholdPin = 18;   //To pin D0 on sound module

int analogValue = 0;    //Variable to store analog reading from sound module
int thresholdStatus;    //Variable to store digital reading from sound module
int baseline;           //Variable to store initial analog reading of background level of noise


void setup() {
  Serial.begin(9600);               //Begin Serial monitor at 9600 baud
  //Sound
  pinMode(soundPin, INPUT);         //Declare pinmode
  pinMode(thresholdPin, INPUT);     //Declare pinmode
  baseline = analogRead(soundPin);
  //Sound captor setup 
  // inutile Serial.begin(9600);
  Serial.print("CRI");
  //Sound
  if (mySensor.begin()) {
    Serial.println("Wait 10 seconds for sensor initialization...");
    delay(10000);
    } 
   else {
     Serial.println("ERROR: Failed to connect to the sensor.");
     while(1);
    }
    //co2 setup
  Serial.println(F("DHTxx test!"));
  dht.begin();
}


void loop() {
  delay(2000);

  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);
  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, h);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);

  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(F("%  Temperature: "));
  Serial.print(t);
  Serial.print(F("°C "));
  Serial.print(f);
  Serial.print(F("°F  Heat index: "));
  Serial.print(hic);
  Serial.print(F("°C "));
  Serial.print(hif);
  Serial.println(F("°F"));
  delay(2000);
  
  // CO2 sensor:
  
    if (mySensor.measure()) {
        Serial.print("CO2 Concentration is ");
        Serial.print(mySensor.ppm);
        Serial.println("ppm");
    } else {
        Serial.println("Sensor communication error.");
    }

    delay(1000);

    // Sound sensor:
      //************** Digital reading - threshold *****************//
  thresholdStatus = digitalRead(thresholdPin);
  Serial.print("Threshold: ");
  Serial.println(thresholdStatus);
  delay(100);
  analogValue = abs(analogRead(soundPin) - baseline); //Analog reading is subtracted with baseline, and abs remove negative values
  Serial.print("Analog Value: ");
  Serial.println(analogValue);

}
