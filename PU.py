import tkinter
from tkinter import *
tkinter.Tcl().eval('info patchlevel')

programa=tkinter.Tk()
programa.geometry("1200x1000")
programa.title("Calculador para Circuitos por unidad")
#Ingresar los datos de potencia Base

datosgm = LabelFrame(programa, text = "Datos de Generadores y Carga")
datosgm.grid()

#infogm = Label(datosgm, text = "Ingrese los valores correspondientes de Potencia y Tensión para cada elemento")
#infogm.grid()

Datosbase = LabelFrame(datosgm, text = "Valores Base")
Datosbase.grid()

L1 = Label(Datosbase, text = "Potencia Base [MVA]")
L1.grid()
E1 = Entry(Datosbase, bd = 5)
E1.grid()
L2 = Label(Datosbase, text = "Tensión Base [kV]")
L2.grid()
E2 = Entry(Datosbase, bd = 5)
E2.grid()

def sel():
   selection = "You selected the option " + str(varRadioButton.get())
   print(selection)
   label.config(text = selection)


varRadioButton = StringVar( value="Ohmnios")
R1 = Radiobutton(datosgm, text = "Ohmnios", variable = varRadioButton, value = "Ohmnios",
                  command = sel)
R1.grid()

R2 = Radiobutton(datosgm, text = "Porcentaje", variable = varRadioButton, value = "Porcentaje",
                  command = sel)
R2.grid()

R3 = Radiobutton(datosgm, text = "Valor PU", variable = varRadioButton, value = "Valor PU",
                  command = sel)
R3.grid()

label = Label(datosgm, text= "SOY UN LABEL")
label.grid()

#Datos del Generador 
DatosG1 = LabelFrame(datosgm, text = "Datos del Generador 1")
DatosG1.grid()

L3 = Label(DatosG1, text = "Potencia [MVA]")
L3.grid()
E3 = Entry(DatosG1, bd = 5)
E3.grid()

mb1 =  Menubutton( datosgm, text = "Reactancia", relief = RAISED )
mb1.grid()
mb1.menu  =  Menu ( mb1, tearoff = 0 )
mb1["menu"]  =  mb1.menu

mayoVar = IntVar()
ketchVar = IntVar()

mb1.menu.add_checkbutton ( label="mayo",
                          variable=mayoVar )
mb1.menu.add_checkbutton ( label="ketchup",
                          variable=mayoVar )
# mb1.grid()

L4 = Label(DatosG1, text = "Tensión Nominal [kV]")
L4.grid()
E4 = Entry(DatosG1, bd = 5)
E4.grid()

#Datos Generador 2
DatosG2 = LabelFrame(datosgm, text = "Datos del Generador 2")
DatosG2.grid()

L5 = Label(DatosG2, text = "Potencia [MVA]")
L5.grid()
E5 = Entry(DatosG2, bd = 5)
E5.grid()

L6 = Label(DatosG2, text = "Tensión Nominal [kV]")
L6.grid()
E6 = Entry(DatosG2, bd = 5)
E6.grid()

#Datos Motor
DatosM = LabelFrame(datosgm, text = "Datos del Generador 1")
DatosM.grid()

L7 = Label(DatosM, text = "Potencia [MVA]")
L7.grid()
E7 = Entry(DatosM, bd = 5)
E7.grid()

L8 = Label(DatosM, text = "Tensión Nominal [kV]")
L8.grid()
E8 = Entry(DatosM, bd = 5)
E8.grid()

def procesarEnOhmnios(pbase,vbase,pg1,vg1,pg2,vg2,pm,vm):
    resultado = float(pbase) / pow(float(vbase),2)
    print("procesarEnOhmnios ", resultado) 

def procesarEnPorcentaje(pbase,vbase,pg1,vg1,pg2,vg2,pm,vm):
    print("procesarEnPorcentaje") 

def procesarEnPU(pbase,vbase,pg1,vg1,pg2,vg2,pm,vm):
    print("procesarEnPU") 


#Obtener valores de las variables
def valores():
    pbase = E1.get()
    print(pbase)
    vbase = E2.get()
    print(vbase)
    pg1 = E3.get()
    print(pg1)
    vg1 = E4.get()
    print(vg1)
    #xg1
    pg2 = E5.get()
    print(pg2)
    vg2 = E6.get()
    print(vg2)
    #Xg1 
    pm = E7.get()
    print(pm)
    vm =E8.get()
    print(vm)
    opcion = varRadioButton.get()
    if (opcion == "Ohmnios"):
        procesarEnOhmnios(pbase,vbase,pg1,vg1,pg2,vg2,pm,vm)
    elif (opcion == "Porcentaje"):
        procesarEnPorcentaje(pbase,vbase,pg1,vg1,pg2,vg2,pm,vm)
    elif (opcion == "Valor PU"):
        procesarEnPU(pbase,vbase,pg1,vg1,pg2,vg2,pm,vm)

    #xm

aceptar = Button(programa, text = "Aceptar", command = valores)
aceptar.grid()


#Calculo de los valores en PU

#Defino que los calculos de los valores en PU
#def calculopu():

#calcular = Button(top, text = "Calcular", command = calculopu)
#calcular.grid()

#Bucle para cerrar la aplicación
programa.mainloop()
