import piezas

# If we use a function, we only need to create move functions and we can continue the game.

def legal_move(before_move, last_move, move_min_max, move_type):
    jugada = [0,0] 
    while jugada == [0,0]:
        if before_move[0] - last_move[0] > move_min_max[0]:
            print("this move is not valid")
            jugada[0] = 0
        else:
            columna = before_move[0]
            jugada[0] = 1

        if before_move[1] - last_move[1] > move_min_max[1]:
            print("this move is not correct")
            jugada[1] = 0
        else:
            fila = before_move[1]
            jugada[1] = 1
        
        nueva_posicion = [columna, fila]
    
    return nueva_posicion

def up_down(last_move, move_min_max, before_move):
    pass

def left_right(columna, fila):
    # columna = movimiento_2
    nueva_posicion = [columna, fila]
    return nueva_posicion

#Elimine los parametros 'movimiento_1' 'movimiento_2'

def diagonales(columna, fila):
    nueva_posicion = [columna, fila]
    return nueva_posicion