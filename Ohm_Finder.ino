int analogPin = 0;
int raw = 0;
float Vin = 5.0;
float V1 = 0;
float V2 = 0;
float I = 0;
float Vout = 0;
float R1 = 1000;
float R2 = 0;
float buffer = 0;

void setup(){
  // initialize serial communication
  // at 9600 bits per second:
  Serial.begin(9600);

} 

void loop(){
  raw = analogRead(analogPin);
  if(raw){
    buffer = raw * Vin;
    Vout = (buffer)/1024.0;
    buffer = (Vin/Vout) - 1;
    R2 = R1 * buffer;
    I = (Vin/(R1+R2)) * 1000.0;
    V1 = (Vin/(R1+R2)) * 1000;
    V2 = (Vin/(R1+R2)) * R2;
    
    Serial.print("Vout: ");
    Serial.println(Vout);
    Serial.print("R2: ");
    Serial.println(R2);
    Serial.print ("I: ");
    Serial.print (I);
    Serial.println (" mA");       
    Serial.print("V1: ");
    Serial.println(V1);
    Serial.print("V2: ");
    Serial.println(V2);
    
  delay(1000);
  }

}