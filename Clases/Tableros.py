
class Tablero:

    def crear_tablero_vacio():
        return [[0]*8 for _ in range(8)]
    
    def tablero_personalizado():
        # Identificador fichas
        # Negros
        # vacio = 0, peon = 1, Torre = 2, Alfil = 3, Caballo = 4, Reina = 5, Rey = 6
        # Blancos
        # peon = 7, Torre = 8, Alfil = 9, Caballo = 10, Reina = 11, Rey = 12
        return [[2, 3, 4, 5, 6, 4, 3, 2],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [7, 7, 7, 7, 7, 7, 7, 7],
                [8, 9, 10, 11, 12, 10, 9, 8]]

