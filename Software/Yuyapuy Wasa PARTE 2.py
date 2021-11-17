
import tkinter as tk #importamos libreria para la interfaz
import serial #importamos libreria para la comunicación de bluetooth

class Window(tk.Tk):
    def __init__(self):
        super().__init__() #heredamos los atributos de tkinter
        self.title("Yuyapuy Wasa") #Nombre de la ventana
        self.geometry('1400x720') #dimensiones de la ventana

        self.var_texto1=tk.StringVar() #declaro variables de texto que se usarán en los entrys
        self.var_texto2=tk.StringVar()
        
        self.yuyframe=tk.Frame(self) #diseño del espacio de la ventana
        self.bottomframe=tk.Frame(self)

        l1=tk.Label(self.yuyframe, text="Yuyapuy Wasa", font=('Arial','60'), justify=tk.CENTER, pady=200) #Nombre del proyecto
        self.b1 = tk.Button(self.bottomframe, text="Nuevo", command=self.Nuevo, padx=60, pady=50) #creo botones
        self.b20=tk.Button(self.bottomframe, text="Buscar", padx=60, pady=50)

        self.yuyframe.pack() #hago el display de los frames
        self.bottomframe.pack()

        l1.pack() #display de los widgets
        self.b1.pack(side=tk.LEFT, padx=100)
        self.b20.pack(side=tk.RIGHT, padx=100)

        port="COM3" #declaro el puerto de comunicación
        BT=serial.Serial(port, 9600) #declaro la comunicación

    def printear (self, event):
        
        positionx = event.x #adquiero las posiciones en donde se da el evento
        positiony = event.y
        if positionx>155 and positionx<225: #uso condicionales para discriminar posiciones en donde se hace click y hacer el display respectivo del electrodo
            if positiony>250 and positiony<320:
                self.canvas2.create_oval(25, 25, 95, 95, fill='yellow', tags="DL1")
                self.canvas2.create_text(60, 60, text = "L1", font = "Times 15", tags = "string")
            if positiony>330 and positiony<400:
                self.canvas2.create_oval(25, 25, 95, 95, fill='yellow', tags="DL2")
                self.canvas2.create_text(60, 60, text = "L2", font = "Times 15", tags = "string")
            if  positiony>410 and positiony<480:
                self.canvas2.create_oval(25, 25, 95, 95, fill='yellow', tags="DL3")
                self.canvas2.create_text(60, 60, text = "L3", font = "Times 15", tags = "string")
        if positionx>275 and positionx<345:
            if positiony>250 and positiony<320:
                self.canvas2.create_oval(25, 25, 95, 95, fill='yellow', tags="DR1")
                self.canvas2.create_text(60, 60, text = "R1", font = "Times 15", tags = "string")
            if positiony>330 and positiony<400:
                self.canvas2.create_oval(25, 25, 95, 95, fill='yellow', tags="DR2")
                self.canvas2.create_text(60, 60, text = "R2", font = "Times 15", tags = "string")
            if  positiony>410 and positiony<480:
                self.canvas2.create_oval(25, 25, 95, 95, fill='yellow', tags="DR3")
                self.canvas2.create_text(60, 60, text = "R3", font = "Times 15", tags = "string")


    def startComm(self):
        BT.write(b'1') #se manda un 1 para que el arduino comience a operar
        for i in range(40): #Se necesitarán 40 adquisiciones para completar los 4 segundos del examen
            input_data=BT.readline() #se lee el valor entrante del bluetooth
            a=input_data.decode() #decodificamos el valor
            time.sleep(0.1) #cada 0.1segundos se adquiere valor
            self.canvas2.create_line() #se crea una linea con los valores
        BT.write(b'0') #Se manda un 0 (o cualquier otro valor) para que el arduino ya no adquiera valores
        

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

        a=92.5
        for i in range(17): #lineas para ilustrar valores ejex
            k=str(i*20)
            lineaa=self.canvas2.create_line(a, 200, a, 500)
            self.canvas2.create_text(a, 515, text=k)
            a+=44.6875

        self.canvas2.create_line(92.5, 200, 807.5, 200) #lineas para el ejey
        self.canvas2.create_line(92.5, 250, 807.5, 250)
        self.canvas2.create_line(92.5, 350, 807.5, 350)
        self.canvas2.create_line(92.5, 450, 807.5, 450)
        self.canvas2.create_line(92.5, 500, 807.5, 500)
        
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
        
        
        


if __name__ == "__main__": 
    window = Window()
    window.mainloop()
