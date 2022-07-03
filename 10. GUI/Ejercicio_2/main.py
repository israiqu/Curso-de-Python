import tkinter
from tkinter import ttk

ventana = tkinter.Tk()

tecnologias = ['Javascript', 'Java', 'Python', 'PHP']
tecnologias_items = tkinter.StringVar(value=tecnologias)
caja = tkinter.Listbox(ventana, height=10, width=50, listvariable=tecnologias_items)
caja.grid(column=0, row=3, sticky=tkinter.W)

texto = ttk.Label(ventana, text="Selecciona la tecnología que te gusta más")
texto.grid(column=0, row=0, padx=5, pady=5)

ventana.mainloop()
