const byte numPins = 7;
void setup() {
  Serial.begin(9600);
  pinMode(7,OUTPUT)
}

void loop() {
  char character = 'a';    
  int ascii = (int) character;
  while(!Serial.available()); // Do nothing until serial input is received
  byte num = Serial.read(); // Get num from somewhere
  for (byte i=0; i<numPins; i++) {
    byte state = bitRead(num, i);
    digitalWrite(7, state);
    Serial.print(state);
    delay(1000);
  }
  Serial.println();