void setup() {
  Serial.begin(9600); // setting serial baudrate
}
void loop() {
  const int bufferLength = 32; //Buffer length for the buffer size to store incoming data.
  char myBuffer[bufferLength]; //Intializing the buffer.
  if (Serial.available() > 0) {
    Serial.readBytesUntil('\n', myBuffer, bufferLength) ;// Reading the incoming data and storing it untill newline charcter. 
    char format[] = "%d,%d,%d"; // Formatting the stored buffer for picking up the integers(sensor data is coming in integer format)
    int Front, Right, Left;  // creating the variables to store the incoming data from relevent sensor to relevant varaible.
    sscanf ( myBuffer, format, &Front, &Right, &Left); // Using sscanf sorting and stroing the values in variables. 
    Serial.print(Front); // sending data string to python in the format of Front|Right|Left/n.
    Serial.print("|");
    Serial.print(Right);
    Serial.print("|");
    Serial.println(Left);
    
  }
}






