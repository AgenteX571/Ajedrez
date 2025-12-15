lista_identificadores = ("casilla vacia", "peon negro", "Torre negra", "Alfil negro", "Caballo negro", "Reina negra", "Rey negro",
                                      "peon blanco", "Torre blanco", "Alfil blanco", "Caballo blanco", "Reina blanca", "Rey blanco")

class Piezas:

    def __init__(self):
        self.movimiento_disponibles = []

    def imprimir(self, num):
        print(lista_identificadores[num])

class peon(Piezas):

    def __init__(self):
        super().__init__()

    def configuracion_movimientos(self, x, y, tablero):
        if tablero[x][y] == 1:
            # primer movimiento, de salida
            if x == 1 and tablero[x + 2][y] == 0:
                self.movimiento_disponibles.append([x+2, y])

            # movimiento normal
            if tablero[x + 1][y] == 0:
                self.movimiento_disponibles.append([x+1, y])

            # consumir ficha
            if y != 0 and y != 7:
                if tablero[x+1][y-1] != 0:
                    self.movimiento_disponibles.append([x+1, y-1])

                if tablero[x+1][y+1] != 0:
                    self.movimiento_disponibles.append([x+1, y+1])
            else:
                if y == 0:
                    if tablero[x+1][y+1] != 0:
                        self.movimiento_disponibles.append([x+1, y+1])
                else:
                    if tablero[x+1][y-1] != 0:
                        self.movimiento_disponibles.append([x+1, y-1])
                
            return self.movimiento_disponibles
        else:
            # peon blanco

            # primer movimiento, de salida
            if x == 6 and tablero[x - 2][y] == 0:
                self.movimiento_disponibles.append([x-2, y])

            # movimiento normal
            if tablero[x - 1][y] == 0:
                self.movimiento_disponibles.append([x-1, y])

            # consumir ficha
            if y != 0 and y != 7:
                if tablero[x-1][y-1] != 0:
                    self.movimiento_disponibles.append([x-1, y-1])

                if tablero[x-1][y+1] != 0:
                    self.movimiento_disponibles.append([x-1, y+1])
            else:
                if y == 0:
                    if tablero[x-1][y+1] != 0:
                        self.movimiento_disponibles.append([x-1, y+1])
                else:
                    if tablero[x-1][y-1] != 0:
                        self.movimiento_disponibles.append([x-1, y-1])
                
            return self.movimiento_disponibles

class Torre(Piezas):
    
    def __init__(self):
        super().__init__()

    def configuracion_movimientos(self, x, y, tablero):
            # Movimientos en x
        for n in range(x+1, 8):
            if tablero[n][y] != 0:
                self.movimiento_disponibles.append([n, y])
                break
            self.movimiento_disponibles.append([n, y])

        for n in range(x-1, -1, -1):
            if tablero[n][y] != 0:
                self.movimiento_disponibles.append([n, y])
                break
            self.movimiento_disponibles.append([n, y])

        # Movimientos en y
        for n in range(y+1, 8):
            if tablero[x][n] != 0:
                self.movimiento_disponibles.append([x, n])
                break
            self.movimiento_disponibles.append([x, n])

        for n in range(y-1, -1, -1):
            if tablero[x][n] != 0:
                self.movimiento_disponibles.append([x, n])
                break
            self.movimiento_disponibles.append([x, n])

        return self.movimiento_disponibles
        

class Alfil(Piezas):
    
    def __init__(self):
        super().__init__()

    def configuracion_movimientos(self, x, y, tablero):
        # Movimientos diagonal derecho
        # Hacia abajo
        for n, i in  zip(range(x+1, 8), range(y+1, 8)):
            if tablero[n][i] != 0:
                self.movimiento_disponibles.append([n, i])
                break
            self.movimiento_disponibles.append([n, i])

        # Hacia arriba
        for n, i in  zip(range(x-1, -1, -1), range(y+1, 8)):
            if tablero[n][i] != 0:
                self.movimiento_disponibles.append([n, i])
                break
            self.movimiento_disponibles.append([n, i])

        # Movimientos diagonal izquierdo
        # Hacia arriba
        for n, i in  zip(range(x+1, 8), range(y-1, -1, -1)):
            if tablero[n][i] != 0:
                self.movimiento_disponibles.append([n, i])
                break
            self.movimiento_disponibles.append([n, i])

        # Movimientos diagonal izquierdo
        # Hacia abajo
        for n, i in  zip(range(x-1, -1, -1), range(y-1, -1, -1)):
            if tablero[n][i] != 0:
                self.movimiento_disponibles.append([n, i])
                break
            self.movimiento_disponibles.append([n, i])

        return self.movimiento_disponibles
    
class Caballo(Piezas):
    
    def __init__(self):
        super().__init__()

    def configuracion_movimientos(self, x, y, tablero):

        # Movimientos en L hacia abajo y hacia arriba
        if (y > 0) and (x <= 5):
            self.movimiento_disponibles.append([x+2, y-1])

        if (y > 0) and (x >= 2):
            self.movimiento_disponibles.append([x-2, y-1])

        if (y < 7) and (x <= 5):
            self.movimiento_disponibles.append([x+2, y+1])

        if (y < 7) and (x >= 2):
            self.movimiento_disponibles.append([x-2, y+1])
        
        # Movimientos en L hacia la derecha y izquierda
        if (y >= 2) and (x <= 6):
            self.movimiento_disponibles.append([x+1, y-2])

        if (y >= 2) and (x >= 1):
            self.movimiento_disponibles.append([x-1, y-2])

        if (y <= 5) and (x <= 6):
            self.movimiento_disponibles.append([x+1, y+2])

        if (x >= 2) and (x >= 1):
            self.movimiento_disponibles.append([x-1, y+2])

        return self.movimiento_disponibles

class Reina(Piezas):
    
    def __init__(self):
        super().__init__()

    def configuracion_movimientos(self, x, y, tablero):
        # Movimientos en x
        for n in range(x+1, 8):
            if tablero[n][y] != 0:
                self.movimiento_disponibles.append([n, y])
                break
            self.movimiento_disponibles.append([n, y])

        for n in range(x-1, -1, -1):
            if tablero[n][y] != 0:
                self.movimiento_disponibles.append([n, y])
                break
            self.movimiento_disponibles.append([n, y])

        # Movimientos en y
        for n in range(y+1, 8):
            if tablero[x][n] != 0:
                self.movimiento_disponibles.append([x, n])
                break
            self.movimiento_disponibles.append([x, n])

        for n in range(y-1, -1, -1):
            if tablero[x][n] != 0:
                self.movimiento_disponibles.append([x, n])
                break
            self.movimiento_disponibles.append([x, n])

        # Movimientos diagonal derecho
        # Hacia abajo
        for n, i in  zip(range(x+1, 8), range(y+1, 8)):
            if tablero[n][i] != 0:
                self.movimiento_disponibles.append([n, i])
                break
            self.movimiento_disponibles.append([n, i])

        # Hacia arriba
        for n, i in  zip(range(x-1, -1, -1), range(y+1, 8)):
            if tablero[n][i] != 0:
                self.movimiento_disponibles.append([n, i])
                break
            self.movimiento_disponibles.append([n, i])

        # Movimientos diagonal izquierdo
        # Hacia arriba
        for n, i in  zip(range(x+1, 8), range(y-1, -1, -1)):
            if tablero[n][i] != 0:
                self.movimiento_disponibles.append([n, i])
                break
            self.movimiento_disponibles.append([n, i])

        # Movimientos diagonal izquierdo
        # Hacia abajo
        for n, i in  zip(range(x-1, -1, -1), range(y-1, -1, -1)):
            if tablero[n][i] != 0:
                self.movimiento_disponibles.append([n, i])
                break
            self.movimiento_disponibles.append([n, i])

        return self.movimiento_disponibles

class Rey(Piezas):
    
    def __init__(self):
        super().__init__()

    def configuracion_movimientos(self, x, y, tablero):
        # movimientos horizontales
        if y < 7:
            self.movimiento_disponibles.append([x, y+1])
        if y > 0:
            self.movimiento_disponibles.append([x, y-1])
        # Movimientos verticales
        if x < 7:
            self.movimiento_disponibles.append([x+1, y])
        if x > 0:
            self.movimiento_disponibles.append([x-1, y])

        # Movimientos diagonales
        # Haciaa abajo
        if (x < 7) and (y < 7):
            self.movimiento_disponibles.append([x+1, y+1])
        if (x < 7) and (y > 0):
            self.movimiento_disponibles.append([x+1, y-1])
        # Hacia arriba
        if (x > 0) and (y < 7):
            self.movimiento_disponibles.append([x-1, y+1])
        if (x > 0) and (y > 0):
            self.movimiento_disponibles.append([x-1, y-1])

        return self.movimiento_disponibles