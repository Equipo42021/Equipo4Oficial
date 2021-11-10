#include "SoftwareSerial.h" //Se incluye la libreria SoftwareSerial.h
SoftwareSerial BT(10, 11);//Conexión TX y RX en estos pins respectivamente

void setup()
{
  Serial.begin(9600); //Inicia la comunicación del monitor serial
  Serial.println("Started");//Avisa al monitor serial que estamos empezando con la comunicación
  BT.begin(9600); //Inicia la comunicación con el módulo de bluetooth
}
void loop()
{
  if (BT.available()) //Si el módulo de bluetooth se quiere comunicar con el arduino...
  {
    Serial.write(BT.read()); //Se presenta la información del módulo de bluetooth en el monitor serial
  }
  
  if (Serial.available()) //Si el monitor serial se quiere comunicar con el módulo de bluetooth...
  {
    BT.write(Serial.read()); //El módulo de bluetooth transmite la información
  }
}
