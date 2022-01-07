
#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "purgatory";
const char* password = "Chiron help";

//Your Domain name with URL path or IP address with path
String serverName = "http://172.20.10.4:8000/sensor/";


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200); 

  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
 
  Serial.println("Timer set to 5 seconds (timerDelay variable), it will take 5 seconds before publishing the first reading.");
}



void loop() {
  // put your main code here, to run repeatedly:
  if(WiFi.status()== WL_CONNECTED){
      HTTPClient http;

      String serverPathco2 = serverName + "co2/" + String(700);

      String serverpathhumidity = serverName + "humidity/" + String(45);
      // Your Domain name with URL path or IP address with path
      http.begin(serverPathco2.c_str());
      Serial.println("LALALALALAAA");
      
      // Send HTTP GET request
      int httpResponseCode = http.GET();
      
      if (httpResponseCode>0) {
        Serial.print("HTTP Response code: ");
        Serial.println(httpResponseCode);
        String payload = http.getString();
        Serial.println(payload);
      }
      else {
        Serial.print("Error code: ");
        Serial.println(httpResponseCode);
      }
      // Free resources
      http.end();
      http.begin(serverpathhumidity.c_str());
      http.GET();
      http.end();
    }
    else {
      Serial.println("WiFi Disconnected");
}
delay(3000);
}
