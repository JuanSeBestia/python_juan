import tkinter
from tkinter import *

root =tkinter.Tk()
root.geometry("300x300")


def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

E1 = Entry(root,bd = 5)

var = IntVar()

R1 = Radiobutton(root, text = "Option 1", variable = var, value = 1,
                  command = sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text = "Option 2", variable = var, value = 2,
                  command = sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text = "Option 3", variable = var, value = 3,
                  command = sel)
R3.pack( anchor = W)

label = Label(root)
label.pack()

numero = var.get()

vn = 10.1
sn = 20.2
vb = 20.5
sb = 25.3

def obtener():

    z1 = float(E1.get())
    if numero==1:
        Vpu = z1*float((sb/pow(vb,2))
    else numero==2:
        Vpu = (pow(vb,2)/sn)*z1*(sb/pow(vb,2))
    else:
        Vpu = z1    

    print (z1)
    print (Vpu)
   

E1.pack()

aceptar = Button(root, text = "Aceptar", command = obtener)
aceptar.pack()

root.mainloop()