import serial #Importamos la libreria Serial


print("Start") #Imprimimos un mensaje para avisar el inicio del programa
port="COM4" #Puerto donde se comunicará
BT=serial.Serial(port, 9600)#Empieza comunicación con la unidad de bluetooth
print("Connected") #Avisamos que ya está conectado
BT.write(b'Hola') #Mandamos un mensaje desde python al arduino
BT.close() #Cerramos la comunicación
print("Done") #Avisamos la finalización de la comunicación
