import tkinter
from tkinter import ttk
import json

with open('errores.json', 'r') as archivo:
    datos=json.load(archivo)

def obtener_desc():
    dato_ingresado = entrada_texto.get()
    for error in datos['errores']:
        if error['codigo'] == dato_ingresado:
            desc_error.config(text=error['desc'])
            break


#ventana creada
ventana = tkinter.Tk()

#titulo ventana
ventana.title("Interfaz de Codigo")
titulo = ttk.Label(ventana, text= "Ingrese El Codigo:  ",font= "calibri 20 bold" ) 
titulo.pack(pady=10, padx= 10)

#entrada de txt
entrada_texto= ttk.Entry(ventana)
entrada_texto.pack(padx=10 , pady= 10  )

#boton Tk
btn_buscar= ttk.Button(ventana, text= "buscar codigo", command= obtener_desc)
btn_buscar.pack(pady=10 ,padx=10)

#desc de busqueda
desc_error= ttk.Label( ventana , text= "")
desc_error.pack(pady= 10)

ventana. mainloop()
