import tkinter
from tkinter import ttk

ventana = tkinter.Tk()

def botonReset(event):
    opcion = None


ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=3)

opcion = tkinter.StringVar()
r1 = ttk.Radiobutton(ventana, text="Javascript", value='1', variable=opcion)
r2 = ttk.Radiobutton(ventana, text="Java", value='2', variable=opcion)
r3 = ttk.Radiobutton(ventana, text="Python", value='3', variable=opcion)

r1.grid(column=0, row=0, padx=5, pady=5)
r2.grid(column=0, row=1, padx=5, pady=5)
r3.grid(column=0, row=2, padx=5, pady=5)

reset_Button = ttk.Button(ventana, text="RESET")
reset_Button.grid(column=0, row=4, sticky=tkinter.E, padx=5, pady=5)
reset_Button.bind('<Button-1>', botonReset)


ventana.mainloop()