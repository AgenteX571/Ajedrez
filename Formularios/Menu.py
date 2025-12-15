import tkinter as tk
from PIL import Image, ImageTk
from Formularios import partida as game

class Menu(tk.Tk):

    def __init__(self):

        super().__init__()
        
        self.config_window()
        self.config_botones()
        self.config_labels()
        self.config_imagenes()

    def config_window(self):
        self.title("Menu")
        self.geometry("500x500")
        self.config(bg="white")
        self.resizable(False, False)

    def config_botones(self):
        self.boton_nueva_partida = tk.Button(self, text="Nueva partida", font=("Hack", 10), bg="white", command=self.comenzar_partida)
        self.boton_nueva_partida.place(x=180, y=400)
        imagen_salida = Image.open(r"Recursos\exit.ico")
        imagen_salida = imagen_salida.resize((20, 20), Image.Resampling.LANCZOS)
        imagen_salida = ImageTk.PhotoImage(imagen_salida)
        self.boton_salir = tk.Button(self, text="Salir", font=("Hack", 10), bg="white", command=self.cerrar_programa, image=imagen_salida, compound="right")
        self.boton_salir.place(x=210, y=435)

    def config_labels(self):
        self.titulo = tk.Label(self, text="Bienvenido a Agedrez", font=("Hack", 14), bg="white")
        self.titulo.place(x=110, y=50)
        self.subtitulo = tk.Label(self, text="creado por Daniel Augusto", font=("Hack", 8), bg="white")
        self.subtitulo.place(x=110, y=80)

    def config_imagenes(self):
        imagen_titulo = Image.open(r"Recursos\foto_titulo.png")
        imagen_titulo = imagen_titulo.resize((280, 280))
        imagen_titulo = ImageTk.PhotoImage(imagen_titulo)
        self.imagen_titulo = tk.Label(self, image=imagen_titulo, bg="white")
        self.imagen_titulo.place(x=110, y=110)

    def comenzar_partida(self):
        self.destroy()
        nueva_partida = game.partida()
        nueva_partida.mainloop()

    def cerrar_programa(self):
        self.quit()