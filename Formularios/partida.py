import tkinter as tk
import copy as cp
from Clases import Fichas
from Clases import Tableros as tbl
from PIL import Image, ImageTk

class partida(tk.Tk):

    def __init__(self):

        super().__init__()

        # Atributos de casilla
        self.posicion_x = 0
        self.posicion_y = 0
        self.ficha_actual = int()
        self.ficha_anterior = int(0)
        self.posiciones_letras = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H"}

        # Metodos del tablero
        self.tablero_partida = cp.deepcopy(tbl.Tablero.tablero_personalizado())
        self.turno_actual = True

        # Atributos tablero
        self.aspectos_ficha = {1:r"imagenes_fichas\peon-negro.png", 2:r"imagenes_fichas\torre-negra.png", 3:r"imagenes_fichas\alfil-negro.png",
                               4:r"imagenes_fichas\caballo-negro.png", 5:r"imagenes_fichas\reina-negra.png", 6:r"imagenes_fichas\rey-negro.png",
                               7:r"imagenes_fichas\peon-blanco.png", 8:r"imagenes_fichas\torre-blanca.png", 9:r"imagenes_fichas\alfil-blanco.png",
                               10:r"imagenes_fichas\caballo-blanco.png", 11:r"imagenes_fichas\reina-blanca.png", 12:r"imagenes_fichas\rey-blanco.png"}
        self.referencia_fichas = []

        #  Metodos de ventana
        self.config_window()
        self.config_label()
        self.config_Tablero()
        self.config_botones()
        self.config_boton_salida()

    def config_window(self):
        # Titulo de la app
        self.title("Ajedrez")
        # Tamaño de la ventana, ventana completa por defecto
        #self.attributes('-fullscreen', True)
        self.resizable(False, False)
        # Otras configuraciones
        self.config(bg="white")

    def config_Tablero(self):
        # frame del tablero de la partida
        self.tablero = tk.Frame(self, width=600, height=600, bg="white")
        self.tablero.pack(side="top", pady=75)

    def config_botones(self):

        fondo = "white"
        for x in range(8):

            if (fondo == "white"):
                fondo = "#ac6843"
            else:
                fondo = "white"

            # Numeracion de letras del tablero
            if (x == 0):
                for i in range(0, 8):
                    letra = tk.Label(self.tablero, font=("Hack", 10), bg="white", width=5, height=3, text=self.posiciones_letras[i])
                    letra.grid(row=0, column=(i + 1))

            # Numeracion del tablero
            numero_linea = tk.Label(self.tablero, font=("Hack", 10), bg="white", width=5, height=3, text=str(x + 1))
            numero_linea.grid(row=x + 1, column=0)

            for y in range(8):
                numero_actual = self.tablero_partida[x][y]
                if numero_actual != 0:
                    imagen_ficha = Image.open(self.aspectos_ficha[self.tablero_partida[x][y]])
                    imagen_ficha = imagen_ficha.resize((40, 40))
                    imagen_ficha = ImageTk.PhotoImage(imagen_ficha)
                    if imagen_ficha not in self.referencia_fichas:
                        self.referencia_fichas.append(imagen_ficha)

                    boton = tk.Button(self.tablero, font=("Hack", 10), fg="red", bg=fondo, width=50, height=48, command=lambda posiciones=(x, y) : self.seleccionar_casilla(posiciones), image=imagen_ficha)
                    boton.grid(row=(x + 1), column=(y + 1))
                else:
                    boton = tk.Button(self.tablero, font=("Hack", 10), fg="red", bg=fondo, width=6, height=3, command=lambda posiciones=(x, y) : self.seleccionar_casilla(posiciones))
                    boton.grid(row=(x + 1), column=(y + 1))

                # Alternacia de fondo entre blanco y negro
                if (fondo == "white"):
                    fondo = "#ac6843"
                else:
                    fondo = "white"

    def config_boton_salida(self):
        # Configuracion del boton de salidas
        imagen_predeterminada = Image.open(r"Recursos\exit.ico")
        imagen_predeterminada = imagen_predeterminada.resize((30, 30))
        imagen_tk = ImageTk.PhotoImage(imagen_predeterminada)
        self.referencia_fichas.append(imagen_tk)

        self.boton_salida = tk.Button(self, font=("Hack", 12), bg="white", width=30, height=28, command=self.cerrar_programa, image=imagen_tk)
        self.boton_salida.pack(side="top")

    def config_label(self):
        self.mostrar_casilla = tk.Label(text=f"{self.posicion_x}, {self.posicion_y}", font=("Hack", 16), bg="white")
        self.mostrar_casilla.pack(side="top", pady=3)

    def modificar_label_casilla(self, casilla):

        posicion_x = casilla[0]
        posicion_y = casilla[1]
        self.ficha_actual = self.tablero_partida[posicion_x][posicion_y]

        self.mostrar_casilla["text"] = f"{posicion_x + 1}, {self.posiciones_letras[posicion_y]}, ficha: {Fichas.lista_identificadores[self.ficha_actual]}"

    def cerrar_programa(self):
        self.quit()

    def determinar_ficha_aliada(self, ficha_actual, ficha_anterior):
        if ficha_anterior in [1, 2, 3, 4, 5, 6] and ficha_actual in [1, 2, 3, 4, 5, 6]:
            return False
        elif ficha_anterior in [7, 8, 9, 10, 11, 12] and ficha_actual in [7, 8, 9, 10, 11, 12]:
            return False
        else:
            return True
        
    def verificar_turno(self, ficha):
        if (ficha in [7, 8, 9, 10, 11, 12]) and (self.turno_actual):
            self.turno_actual = False
            return True
        
        if (ficha in [1, 2, 3, 4, 5, 6]) and not (self.turno_actual):
            self.turno_actual = True
            return True

        return False

    def seleccionar_casilla(self, casilla):
        self.modificar_label_casilla(casilla)

        if self.ficha_actual != 0 and self.ficha_anterior == 0:
            # sistema de turnos
            if self.verificar_turno(self.ficha_actual):
                # Guarda la posicion de la ficha a mover
                self.posicion_x = casilla[0]
                self.posicion_y = casilla[1]
                self.ficha_anterior = cp.deepcopy(self.ficha_actual)
            else:
                self.ficha_actual = 0
                if self.turno_actual:
                    self.mostrar_casilla["text"] = "Es turno de los blancos"
                else:
                    self.mostrar_casilla["text"] = "Es turno de los negros"
        else:
            if self.ficha_anterior != 0:
            # Administrador de movimientos : asigna la clase de movimientos
                match self.ficha_anterior:
                    case 1 | 7:
                        movimientos = Fichas.peon()
                    case 2 | 8:
                        movimientos = Fichas.Torre()
                    case 3 | 9:
                        movimientos = Fichas.Alfil()
                    case 4 | 10:
                        movimientos = Fichas.Caballo()
                    case 5 | 11:
                        movimientos = Fichas.Reina()
                    case 6 | 12:
                        movimientos = Fichas.Rey()

                # Flujo de movimientos del tablero
                if (movimientos is not None) and (self.determinar_ficha_aliada(self.ficha_actual, self.ficha_anterior)):
                    #                                metodo de clase de la ficha
                    movimientos_validos = movimientos.configuracion_movimientos(self.posicion_x, self.posicion_y, self.tablero_partida)
                    if list(casilla) in movimientos_validos:
                        # Determinar si un peon se transforma en reina
                        if (self.ficha_anterior == 1 or self.ficha_anterior == 7) and (casilla[0] == 7 or casilla[0] == 0):
                            if self.ficha_anterior == 1:
                                self.tablero_partida[casilla[0]][casilla[1]] = 5
                            else:
                                self.tablero_partida[casilla[0]][casilla[1]] = 11
                        else:
                            self.tablero_partida[casilla[0]][casilla[1]] = cp.deepcopy(self.ficha_anterior)

                        self.tablero_partida[self.posicion_x][self.posicion_y] = 0
                        self.ficha_actual = cp.copy(self.ficha_anterior)
                        self.ficha_anterior = 0
                        self.config_botones()
                else:
                    self.mostrar_casilla["text"] = "Movimiento no valido"
                    self.ficha_actual = cp.copy(self.ficha_anterior)
                    self.ficha_anterior = 0