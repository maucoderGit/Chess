
#necesitamos una funcion que determine si no es legal, y que luego usemos en cada jugada

def legal_move(pos_anterior, pos_actual, legal):
    resta = pos_actual - pos_anterior
    if resta > legal:
        jugada = ("No es legal")
    else:
        jugada = ("es legal")
    return jugada

#Decidi que es mejor hacer la función en un bucle y que 
#verifique si es legal o no hasta que se decida un resultado

def up_down(last_move, move_min_max, before_move):
    pass

def left_right(columna, fila):
    # columna = movimiento_2
    nueva_posicion = [columna, fila]
    return nueva_posicion

columna = int(input("cual es la columna: "))
fila = int(input("cual es la fila: "))
culumna_ant = 1
fila_ant = 1
pieza = 1
columna = legal_move(culumna_ant , columna , pieza)
print (columna)
#Elimine los parametros 'movimiento_1' 'movimiento_2'

def diagonales(columna, fila):
    nueva_posicion = [columna, fila]
    return nueva_posicion