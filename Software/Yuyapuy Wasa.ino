// C++ code
//

//Declaro variables a usar:

int sum1=0;
int sum2=0;
int sum3=0;
int sum4=0;
int sum5=0;
int sum6=0;

int i=0;

int media1=0;
int media2=0;
int media3=0;
int media4=0;
int media5=0;
int media6=0;

int sumaL1;
int sumaL2;
int sumaL3;

int sumaR1;
int sumaR2;
int sumaR3;

int a=0;

void setup()
{
  Serial.begin(9600); //Declaro la velocidad de comunicación del
  					  //monitor serial
  DDRD=0xFC; //Declaro mis outputs
}

int suma(int suma, int val, String emg) //Función para hacer suma total
{
  Serial.print(emg); //imprimo el nombre del sensor
  Serial.print(": "); //:
  Serial.print(val); //Imprimo el valor adquirido
  suma=suma+val; //Calculo la suma total
  return suma; //Retorno el valor de la suma
}

int prom (int suma, int i) //Función para calcular promedio
{
  int promedio=suma/i; //Calculo promedio del sensor
  Serial.print("\t prom= "); //Imprimo label
  Serial.println(promedio); //Imprimo valor del promedio
  return promedio; //retorno valor promedio
}

void comparar(int media1, int media2, int op1, int op2) //Función para comparar promedios
{
  if (media1>media2) //Si el prom sensor 1 es mayor que el
  {					 //del sensor 2 se prende el led correspondiente
    digitalWrite(op1, HIGH);
    digitalWrite(op2, LOW);
  }
  else
  {
    digitalWrite(op1, LOW);
    digitalWrite(op2, HIGH);
  }
}

void loop()
{
  if (Serial.available()>0) //Si hay un valor en el monitor serial...
  {
    a=Serial.read(); //Leo dicho valor
    while (a=='1') //Si el valor es 1 procedo a correr el bucle
    {
      i=i+1; //Contador que nos ayudará al calculo del promedio
      sumaL1=suma(sumaL1, analogRead(A0), "L1"); //Calculo suma del sensor L1
      media1=prom(sumaL1, i); //Calculo media del sensor L1
      sumaR1=suma(sumaR1, analogRead(A1), "R1"); //Calculo suma del sensor R1
      media2=prom(sumaR1, i); //Calculo media del sensor R1
      comparar(media1, media2, 3, 2); //Comparo las medias y enciendo el led que corresponde

      //De esta manera se procede con los otros 4 sensores EMG.
      
      sumaL2=suma(sumaL2, analogRead(A2), "L2");
      media3=prom(sumaL2, i);
      sumaR2=suma(sumaR2, analogRead(A3), "R2");
      media4=prom(sumaR2, i);
      comparar(media3, media4, 4, 5);
      
      
      sumaL3=suma(sumaL3, analogRead(A4), "L3");
      media5=prom(sumaL3, i);
      sumaR3=suma(sumaR3, analogRead(A5), "R3");
      media6=prom(sumaR3, i);
      comparar(media5, media6, 6, 7);
      
      if (Serial.available()) //En el caso se encuentre otro valor...
      {
        a=Serial.read(); //Se lee el valor para terminar de leer el bucle
      }
      
      delay(1000); //Espera de 1000 (solo para tener orden)
    }
    PORTD=0x00; //Se apagan los leds en caso se salga del bucle
  }
}
