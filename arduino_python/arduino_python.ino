String serData;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT); // Set pin 13 as an output
  Serial.println("Arduino is ready!");
}

void loop() {
  while(Serial.available() > 0){
    char rec = Serial.read();
    serData += rec;

    if (rec=='\n'){
      Serial.print("Message received: ");
      Serial.println(serData);
      // Check the received message and toggle LED accordingly
      if (serData == "activate_led\n") {
        digitalWrite(13, HIGH); // Turn on the LED
        Serial.println("LED activated");
      } else if (serData == "deactivate_led\n") {
        digitalWrite(13, LOW); // Turn off the LED
        Serial.println("LED deactivated");
      }
      serData="";
    }
  }

  delay(10);
}
