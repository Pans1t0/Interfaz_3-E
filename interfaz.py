import tkinter
from tkinter import ttk
#ventana creada
ventana = tkinter.Tk()

#titulo ventana
ventana.title("Interfaz de Codigo")
titulo = ttk.Label(ventana, text= "Ingrese el codigo:  ",font= "calibri 20 bold" ) 
titulo.pack(pady=10, padx= 10)

#entrada de txt
entrada_texto= ttk.Entry(ventana)
entrada_texto.pack(padx=10 , pady= 10  )

#boton Tk
btn_buscar= ttk.Button(ventana, text= "buscar codigo")
btn_buscar.pack(pady=10 ,padx=10)

#desc de busqueda
desc_error= ttk.Label( ventana , text= "")
desc_error.pack(pady= 10)

ventana. mainloop()
