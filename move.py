
#necesitamos una funcion que determine si no es legal, y que luego usemos en cada jugada

def letras_a_numeros(columna):

    letras = ["a","b","c","d","e","f","g","h"]
    count = 0
    for i in letras:
        count += 1
        if columna == i:
            columna = count

    numeros = [1,2,3,4,5,6,7,8]
    count = 0
    for i in numeros:
        count += 1
        if count == columna:
            columna = i
    return columna

def numeros_a_letras(columna):
    letras = ["a","b","c","d","e","f","g","h"]
    count = 0
    for i in letras:
        count += 1
        if count == columna:
            columna = i
    return columna

def legal_move(posicion_anterior, posicion_actual, legal):
    resta = posicion_actual - posicion_anterior
    if resta > legal:
        jugada = False
    else:
        jugada = True
    return jugada

#Decidi que es mejor hacer la función en un bucle y que 
#verifique si es legal o no hasta que se decida un resultado

def movimiento_columnas(fila_anterior, fila_actual):
    if fila_anterior != fila_actual:
        vertical = True
    else:
        vertical = False
    return vertical    


def movimiento_filas(columna_anterior, columna_actual):
    if columna_anterior != columna_actual:
        horizontal = True
    else:
        horizontal = False
    return horizontal


def tipo_de_movimiento(horizontal, vertical):
    if horizontal == True and vertical == True:
        movimiento = "diagonal"
    elif horizontal == True and vertical == False:
        movimiento = "horizontal"
    else:
        movimiento = "fila"
    return movimiento


def Preguntar_jugada(posicion_anterior, caso, legal):
    jugada_anterior = posicion_anterior
    pieza = legal

    jugada = int(input("cual es la " + caso + " : "))
    jugada_legal = legal_move(jugada_anterior, jugada, pieza)

    if jugada_legal == False:
        print("no es valido")
        jugada = Preguntar_jugada(jugada_anterior, caso ,pieza)
    else:     
        return jugada
    
    return jugada

def run():

    pieza = 1
    columna_anterior = 1
    fila_anterior = 1
    columna = columna_anterior
    fila= fila_anterior

    while columna == columna_anterior and fila == fila_anterior:
        print("haz un movimiento") 
        columna = Preguntar_jugada(columna_anterior, "columna",pieza)
        fila = Preguntar_jugada(fila_anterior,"fila",pieza)

    mov_vertical = movimiento_columnas(fila_anterior,fila)
    mov_horizontal = movimiento_filas(columna_anterior, columna)

    movimiento = tipo_de_movimiento(mov_horizontal, mov_vertical)

    columna = numeros_a_letras(columna)
    print("La nueva posición es: ", columna , fila, "en " + movimiento)

#Decidi crear una función recursiva, para ver si era legal o no.
#Asi todo el código sera mas estetíco, ademas de que compila mejor :)    

if __name__ == "__main__":
    run()