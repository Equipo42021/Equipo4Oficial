
import tkinter as tk #importamos libreria para la interfaz
import serial #importamos libreria para la comunicación de bluetooth
import codecs
import time


speed=9600
port="COM4" #declaro el puerto de comunicación
BT=serial.Serial(port, speed, timeout=1) #declaro la comunicación



class Window(tk.Tk):
    def __init__(self):
        super().__init__() #heredamos los atributos de tkinter
        self.title("Yuyapuy Wasa") #Nombre de la ventana
        self.geometry('1400x720') #dimensiones de la ventana

        self.var_texto1=tk.StringVar() #declaro variables de texto que se usarán en los entrys
        self.var_texto2=tk.StringVar()

        self.listaprueba=[500,900]

        self.listaEmg1=[]
        self.listaEmg2=[]
        self.listaEmg3=[]
        self.listaEmg4=[]
        self.listaEmg5=[]
        self.listaEmg6=[]
        
        self.yuyframe=tk.Frame(self) #diseño del espacio de la ventana
        self.bottomframe=tk.Frame(self)

        l1=tk.Label(self.yuyframe, text="Yuyapuy Wasa", font=('Arial','60'), justify=tk.CENTER, pady=200) #Nombre del proyecto
        self.b1 = tk.Button(self.bottomframe, text="Nuevo", command=self.Nuevo, padx=60, pady=50) #creo botones
        #self.b20=tk.Button(self.bottomframe, text="Buscar", padx=60, pady=50)

        self.yuyframe.pack() #hago el display de los frames
        self.bottomframe.pack()

        l1.pack() #display de los widgets
        self.b1.pack(side=tk.LEFT, padx=100)
        #self.b20.pack(side=tk.RIGHT, padx=100)

        


    def printear (self, event):
        
        positionx = event.x #adquiero las posiciones en donde se da el evento
        positiony = event.y
        if positionx>155 and positionx<225: #uso condicionales para discriminar posiciones en donde se hace click y hacer el display respectivo del electrodo
            if positiony>250 and positiony<320:
                self.canvas2.create_oval(25, 25, 95, 95, fill='yellow', tags="DL1")
                self.canvas2.create_text(60, 60, text = "L1", font = "Times 15", tags = "stringL1")


                
                self.canvas3.grid_forget()
                self.canvas4.grid_forget()
                self.canvas5.grid_forget()
                self.canvas6.grid_forget()
                self.canvas7.grid_forget()
                
                self.canvas2.grid(row=2, column=2, rowspan=2)
            if positiony>330 and positiony<400:
                self.canvas3.create_oval(25, 25, 95, 95, fill='yellow', tags="DL2")
                self.canvas3.create_text(60, 60, text = "L2", font = "Times 15", tags = "string")
                
                self.canvas2.grid_forget()
                self.canvas4.grid_forget()
                self.canvas5.grid_forget()
                self.canvas6.grid_forget()
                self.canvas7.grid_forget()

                self.canvas3.grid(row=2, column=2, rowspan=2)
            if  positiony>410 and positiony<480:
                self.canvas4.create_oval(25, 25, 95, 95, fill='yellow', tags="DL3")
                self.canvas4.create_text(60, 60, text = "L3", font = "Times 15", tags = "string")
                
                self.canvas2.grid_forget()
                self.canvas3.grid_forget()
                self.canvas5.grid_forget()
                self.canvas6.grid_forget()
                self.canvas7.grid_forget()

                self.canvas4.grid(row=2, column=2, rowspan=2)
        if positionx>275 and positionx<345:
            if positiony>250 and positiony<320:
                self.canvas5.create_oval(25, 25, 95, 95, fill='yellow', tags="DR1")
                self.canvas5.create_text(60, 60, text = "R1", font = "Times 15", tags = "string")

                self.canvas2.grid_forget()
                self.canvas3.grid_forget()
                self.canvas4.grid_forget()
                self.canvas6.grid_forget()
                self.canvas7.grid_forget()
                
                self.canvas5.grid(row=2, column=2, rowspan=2)
            if positiony>330 and positiony<400:
                self.canvas6.create_oval(25, 25, 95, 95, fill='yellow', tags="DR2")
                self.canvas6.create_text(60, 60, text = "R2", font = "Times 15", tags = "string")

                self.canvas2.grid_forget()
                self.canvas3.grid_forget()
                self.canvas4.grid_forget()
                self.canvas5.grid_forget()
                self.canvas7.grid_forget()
                
                self.canvas6.grid(row=2, column=2, rowspan=2)
            if  positiony>410 and positiony<480:
                self.canvas7.create_oval(25, 25, 95, 95, fill='yellow', tags="DR3")
                self.canvas7.create_text(60, 60, text = "R3", font = "Times 15", tags = "string")

                self.canvas2.grid_forget()
                self.canvas3.grid_forget()
                self.canvas4.grid_forget()
                self.canvas5.grid_forget()
                self.canvas6.grid_forget()
                
                self.canvas7.grid(row=2, column=2, rowspan=2)


    def startComm(self):

        print('a')

        
        BT.write(b'1') #se manda un 1 para que el arduino comience a operar
        t=92.5
        for h in range(5):
            
            input_data=BT.readline()
            input_data=input_data.decode()
            print(input_data)
            lista=input_data.split(',')
            self.listaEmg1.append(lista[0])
            self.listaEmg2.append(lista[1])
            self.listaEmg3.append(lista[2])
            self.listaEmg4.append(lista[3])
            self.listaEmg5.append(lista[4])
            self.listaEmg6.append(lista[5])
            if h>0:
                self.canvas2.create_line(t,500-300*int(self.listaEmg1[-2])/1023, t+8.9375,500-300*int(self.listaEmg1[-1])/1023)
                self.canvas3.create_line(t,500-300*int(self.listaEmg2[-2])/1023, t+8.9375,500-300*int(self.listaEmg2[-1])/1023)
                self.canvas4.create_line(t,500-300*int(self.listaEmg3[-2])/1023, t+8.9375,500-300*int(self.listaEmg3[-1])/1023)
                self.canvas5.create_line(t,500-300*int(self.listaEmg4[-2])/1023, t+8.9375,500-300*int(self.listaEmg4[-1])/1023)
                self.canvas6.create_line(t,500-300*int(self.listaEmg5[-2])/1023, t+8.9375,500-300*int(self.listaEmg5[-1])/1023)
                self.canvas7.create_line(t,500-300*int(self.listaEmg6[-2])/1023, t+8.9375,500-300*int(self.listaEmg6[-1])/1023)

                t=t+8.9375
            time.sleep(0.1)
            



            
            #print(t)
        self.canvas2.create_text(450, 150, text=str(lista[6]))
        self.canvas3.create_text(450, 150, text=str(lista[7]))
        self.canvas4.create_text(450, 150, text=str(lista[8]))
        self.canvas5.create_text(450, 150, text=str(lista[9]))
        self.canvas6.create_text(450, 150, text=str(lista[10]))
        self.canvas7.create_text(450, 150, text=str(lista[11]))

        self.canvas2.create_oval(25, 25, 95, 95, fill='yellow', tags="DL1")
        self.canvas2.create_text(60, 60, text = "L1", font = "Times 15", tags = "stringL1")

        self.canvas2.grid(row=2, column=2, rowspan=2)


        BT.write(b'0') #Se manda un 0 (o cualquier otro valor) para que el arduino ya no adquiera valores
        #for i in range (80):
        #    input_data=BT.readline()
        #while True:
            #input_data=BT.readline()
            #input_data=input_data.split(b',')
            #self.lista1.append(input_data[1])
            #print(input_data)
            #print(self.lista1)
            
            #print(codecs.getdecoder(input_data))
            #print(codecs.decode(input_data, encoding='utf-8', errors='strict'))
            #print(input_data.decode('utf-8'))
            #print('a')
            #if input_data!="":
            #    print('b')
        #print(input_data.decode())
        
       #for i in range(40): #Se necesitarán 40 adquisiciones para completar los 4 segundos del examen
       #     input_data=BT.readline() #se lee el valor entrante del bluetooth
##     #       a=input_data.decode() #decodificamos el valor
       #     print(input_data)
       #     time.sleep(0.1) #cada 0.1segundos se adquiere valor
            #self.canvas2.create_line() #se crea una linea con los valores
       
        

    def endComm(self):
        self.ex.withdraw() #se termina el examen y se pasa a ventana principal
        self.deiconify()
        



    def Nuevo(self):
        self.withdraw() #se cierra la ventana principal
        self.New=tk.Toplevel() #se crea una nueva ventana
        self.New.geometry('1400x720') #dimensiones de la nueva ventana
        l2=tk.Label(self.New, text='Datos del paciente', font=('Arial', '40')) #label
        l2.pack() #display del label

        self.e1 = tk.Entry(self.New, textvariable=self.var_texto1, width=50) #Se definen 2 entrys que se usarán para el input de los datos del paciente
        
        self.e2=tk.Entry(self.New, textvariable=self.var_texto2, width=50)
        
        self.l3=tk.Label(self.New, text='Nombres y apellidos: ', pady=10) #título de cada entry
        self.l4=tk.Label(self.New, text='DNI: ', pady=10)

        
        self.l3.pack(pady=10) #display de cada objeto en la ventana
        self.e1.pack(pady=10)
        self.l4.pack(pady=10)
        self.e2.pack(pady=10)
        
        b2=tk.Button(self.New, text='Continuar', command= self.examen, padx=25, pady=12) #boton para continuar con la siguiente ventana
        b2.pack(pady=10)


    def examen(self):
        a=self.var_texto1.get() #adquirimos los datos del paciente
        b=self.var_texto2.get()
        self.var_texto1.set("") #borramos todo
        self.var_texto2.set("")
        print(a) #hacemos print de lo adquirido
        print(b)
        self.New.withdraw() #cerramos ventana
        self.ex=tk.Toplevel() #creamos nueva ventana para el examen

        l5=tk.Label(self.ex, text="Paciente:", font=('Arial', '10')) #información del paciente
        l6=tk.Label(self.ex, text=a )
        l7=tk.Label(self.ex, text="DNI:", font=('Arial', '10'))
        l8=tk.Label(self.ex, text=b)
        
        l5.grid(row=0, column=0) #organización de la ventana
        l6.grid(row=0, column=1)
        l7.grid(row=1, column=0)
        l8.grid(row=1, column=1)
        
        
        self.ex.geometry('1400x720') #dimensiones de la ventana

        
        self.canvas1=tk.Canvas(self.ex, width=500, height=500, background='white') #gráfica
        self.canvas1.grid(row=2, column=0, columnspan=2, sticky=tk.N)

        self.canvas2=tk.Canvas(self.ex, width=900, height=700, background='white')
        
        self.canvas2.grid(row=2, column=2, rowspan=2)

        self.canvas3=tk.Canvas(self.ex, width=900, height=700, background='white')
        self.canvas4=tk.Canvas(self.ex, width=900, height=700, background='white')
        self.canvas5=tk.Canvas(self.ex, width=900, height=700, background='white')
        self.canvas6=tk.Canvas(self.ex, width=900, height=700, background='white')
        self.canvas7=tk.Canvas(self.ex, width=900, height=700, background='white')

        a=92.5
        for i in range(17): #lineas para ilustrar valores ejex
            k=str(i*20)
            lineaa=self.canvas2.create_line(a, 200, a, 500)
            lineaa=self.canvas3.create_line(a, 200, a, 500)
            lineaa=self.canvas4.create_line(a, 200, a, 500)
            lineaa=self.canvas5.create_line(a, 200, a, 500)
            lineaa=self.canvas6.create_line(a, 200, a, 500)
            lineaa=self.canvas7.create_line(a, 200, a, 500)
            self.canvas2.create_text(a, 515, text=k)
            a+=44.6875

        self.canvas2.create_text(450, 550, text='Tiempo (0.0125 s)')
        self.canvas2.create_text(390, 150, text='Promedio: ')

        self.canvas3.create_text(450, 550, text='Tiempo (0.0125 s)')
        self.canvas3.create_text(390, 150, text='Promedio: ')

        self.canvas4.create_text(450, 550, text='Tiempo (0.0125 s)')
        self.canvas4.create_text(390, 150, text='Promedio: ')

        self.canvas5.create_text(450, 550, text='Tiempo (0.0125 s)')
        self.canvas5.create_text(390, 150, text='Promedio: ')

        self.canvas6.create_text(450, 550, text='Tiempo (0.0125 s)')
        self.canvas6.create_text(390, 150, text='Promedio: ')

        self.canvas7.create_text(450, 550, text='Tiempo (0.0125 s)')
        self.canvas7.create_text(390, 150, text='Promedio: ')

        self.canvas2.create_text(80, 250, text=str(854))
        self.canvas2.create_text(80, 350, text=str(512))
        self.canvas2.create_text(80, 450, text=str(170))
        self.canvas2.create_text(80, 200, text=str(1023))
        self.canvas2.create_text(40, 350, text='Amplitud')

        self.canvas3.create_text(80, 250, text=str(854))
        self.canvas3.create_text(80, 350, text=str(512))
        self.canvas3.create_text(80, 450, text=str(170))
        self.canvas3.create_text(80, 200, text=str(1023))
        self.canvas3.create_text(40, 350, text='Amplitud')
        
        self.canvas4.create_text(80, 250, text=str(854))
        self.canvas4.create_text(80, 350, text=str(512))
        self.canvas4.create_text(80, 450, text=str(170))
        self.canvas4.create_text(80, 200, text=str(1023))
        self.canvas4.create_text(40, 350, text='Amplitud')

        self.canvas5.create_text(80, 250, text=str(854))
        self.canvas5.create_text(80, 350, text=str(512))
        self.canvas5.create_text(80, 450, text=str(170))
        self.canvas5.create_text(80, 200, text=str(1023))
        self.canvas5.create_text(40, 350, text='Amplitud')

        self.canvas6.create_text(80, 250, text=str(854))
        self.canvas6.create_text(80, 350, text=str(512))
        self.canvas6.create_text(80, 450, text=str(170))
        self.canvas6.create_text(80, 200, text=str(1023))
        self.canvas6.create_text(40, 350, text='Amplitud')

        self.canvas7.create_text(80, 250, text=str(854))
        self.canvas7.create_text(80, 350, text=str(512))
        self.canvas7.create_text(80, 450, text=str(170))
        self.canvas7.create_text(80, 200, text=str(1023))
        self.canvas7.create_text(40, 350, text='Amplitud')

        self.canvas2.create_line(92.5, 200, 807.5, 200) #lineas para el ejey
        self.canvas2.create_line(92.5, 250, 807.5, 250)
        self.canvas2.create_line(92.5, 350, 807.5, 350)
        self.canvas2.create_line(92.5, 450, 807.5, 450)
        self.canvas2.create_line(92.5, 500, 807.5, 500)

        self.canvas3.create_line(92.5, 200, 807.5, 200) #lineas para el ejey
        self.canvas3.create_line(92.5, 250, 807.5, 250)
        self.canvas3.create_line(92.5, 350, 807.5, 350)
        self.canvas3.create_line(92.5, 450, 807.5, 450)
        self.canvas3.create_line(92.5, 500, 807.5, 500)

        self.canvas4.create_line(92.5, 200, 807.5, 200) #lineas para el ejey
        self.canvas4.create_line(92.5, 250, 807.5, 250)
        self.canvas4.create_line(92.5, 350, 807.5, 350)
        self.canvas4.create_line(92.5, 450, 807.5, 450)
        self.canvas4.create_line(92.5, 500, 807.5, 500)

        self.canvas5.create_line(92.5, 200, 807.5, 200) #lineas para el ejey
        self.canvas5.create_line(92.5, 250, 807.5, 250)
        self.canvas5.create_line(92.5, 350, 807.5, 350)
        self.canvas5.create_line(92.5, 450, 807.5, 450)
        self.canvas5.create_line(92.5, 500, 807.5, 500)

        self.canvas6.create_line(92.5, 200, 807.5, 200) #lineas para el ejey
        self.canvas6.create_line(92.5, 250, 807.5, 250)
        self.canvas6.create_line(92.5, 350, 807.5, 350)
        self.canvas6.create_line(92.5, 450, 807.5, 450)
        self.canvas6.create_line(92.5, 500, 807.5, 500)

        self.canvas7.create_line(92.5, 200, 807.5, 200) #lineas para el ejey
        self.canvas7.create_line(92.5, 250, 807.5, 250)
        self.canvas7.create_line(92.5, 350, 807.5, 350)
        self.canvas7.create_line(92.5, 450, 807.5, 450)
        self.canvas7.create_line(92.5, 500, 807.5, 500)
        
        self.canvas1.create_oval(155, 250, 225, 320, fill='red', tags="CL1") #creamos los íconos de los electrodos
        self.canvas1.create_oval(155, 330, 225, 400, fill='red', tags="CL2")
        self.canvas1.create_oval(155, 410, 225, 480, fill='red', tags="CL3")
        
        self.canvas1.create_oval(275, 250, 345, 320, fill='blue', tags="CR1")
        self.canvas1.create_oval(275, 330, 345, 400, fill='blue', tags="CR2")
        self.canvas1.create_oval(275, 410, 345, 480, fill='blue', tags="CR3")
        
        self.canvas1.create_text(310, 285, text = "R1", font = "Times 15", tags = "R1") #etiquetas de cada electrodo
        self.canvas1.create_text(310, 365, text = "R2", font = "Times 15", tags = "R2")
        self.canvas1.create_text(310, 445, text = "R3", font = "Times 15", tags = "R3")

        self.canvas1.create_text(190, 285, text = "L1", font = "Times 15", tags = "L1")
        self.canvas1.create_text(190, 365, text = "L2", font = "Times 15", tags = "L2")
        self.canvas1.create_text(190, 445, text = "L3", font = "Times 15", tags = "L3")

        b3=tk.Button(self.ex, text="Empezar", padx=10, pady=20, command=self.startComm) #al apretar start se empieza el examen
        b4=tk.Button(self.ex, text="Terminar", padx=10, pady=20, command=self.endComm) #se termina el examen
        
        b3.grid(row=3, column=0, sticky=tk.N) #organización de los botones
        b4.grid(row=3, column=1, sticky=tk.N)
        
        
        self.canvas1.bind('<Button-1>', self.printear) #lo que va a hacer que se puedan seleccionar los electrodos
        
        #while BT.readline()!="":
            #input_data=BT.readline()
            #input_data=input_data.split(b',')
            #self.lista1.append(input_data[1])
            #print(input_data)
        
        
        
if __name__ == "__main__": 
    window = Window()
    window.mainloop()
