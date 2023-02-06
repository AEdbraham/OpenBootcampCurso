from tkinter import *
from tkinter import ttk

def selec():
    monitor.config(text = "Opción {}".format(opcion.get() ) )

def reinicio():
    opcion.set(-1)
    monitor.config(text="")

root = Tk()
root.config(bd=50)

opcion = IntVar() # Como StrinVar pero en entero

Radiobutton(root, text="Opción 1", variable=opcion, 
            value=1, command=selec).pack()
Radiobutton(root, text="Opción 2", variable=opcion,
            value=2, command=selec).pack()
Radiobutton(root, text="Opción 3", variable=opcion, 
            value=3, command=selec).pack()

boton = ttk.Button(text="Reiniciar", command=reinicio)
boton.place(x=5, y=105)

monitor = Label(root)
monitor.pack()

root.mainloop()