import tkinter as tk
import copy as cp
from PIL import Image, ImageTk

ventana = tk.Tk()
ventana.geometry("300x300")
ventana.config(bg="green")

contenedor = tk.Frame(ventana, width=150, height=150, bg="white")
contenedor.pack(anchor="center", expand=True)
contenedor.pack_propagate(False)

imagenes = {0:r"imagenes_fichas\peon-negro.png", 1:r"imagenes_fichas\reina-negra.png", 2:r"imagenes_fichas\rey-negro.png"}
fichas = []

#boton = tk.Button(contenedor,  width=30, height=30, image=imagen_peon)
#boton.pack(pady=1)

#boton1 = tk.Button(contenedor,  width=30, height=30, image=imagen_peon)
#boton1.pack(pady=1)

#boton2 = tk.Button(contenedor,  width=30, height=30, image=imagen_peon)
#boton2.pack(pady=1)

def mostrar(num):
    print(num) 

for x in range(3):
    imagen_ficha = Image.open(imagenes[x])
    imagen_ficha = imagen_ficha.resize((30, 30))
    imagen_ficha = ImageTk.PhotoImage(imagen_ficha)
    fichas.append(imagen_ficha)

    boton = tk.Button(contenedor,  width=30, height=30, image=imagen_ficha, command=lambda num = x : mostrar(num))
    boton.pack(pady=1)

ventana.mainloop()

# hola