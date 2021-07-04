import tablero
import move

#Ajustando los valores y posición inicial de las piezas blancas.

def rey(columna, fila, jaque, pieza_rey, posicion):
    if posicion[columna] != columna and posicion[fila] != fila: 
        move.diagonales(columna, fila)

pieza_rey = {
    "nombre" : "Rey",
    "movimiento_min" : 1,
    "movimiento_max" : 1,
    "Jaque" : False
}

dama_blanca = {
    "nombre" : "Dama",
    "posicion" : [1,4],
    "valor" : 9,
    "estado" : True
}

alfil_blanco_1 = {
    "nombre" : "Alfil",
    "posicion" : [1,3],
    "valor" : 3,
    "estado" : True
}

alfil_blanco_2 = {
    "nombre" : "Alfil",
    "posicion" : [1,6],
    "valor" : 3,
    "estado" : True
}

caballo_blanco_1 = {
    "nombre" : "Caballo",
    "posicion" : [1,2],
    "valor" : 3,
    "estado" : True
}

caballo_blanco_2 = {
    "nombre" : "Caballo",
    "posicion" : [1,7],
    "valor" : 3,
    "estado" : True
}

torre_blanca_1 = {
    "nombre" : "Torre",
    "posicion" : [1,1],
    "valor" : 5,
    "estado" : True
}

torre_blanca_2 = {
    "nombre" : "Torre",
    "posicion" : [1,8],
    "valor" : 5,
    "estado" : True
}

peon_blanco_1 = {
    "nombre" : "peon",
    "posicion" : [2,1],
    "valor" : 1,
    "estado" : True
}

peon_blanco_2 = {
    "nombre" : "peon",
    "posicion" : [2,2],
    "valor" : 1,
    "estado" : True
}

peon_blanco_3 = {
    "nombre" : "peon",
    "posicion" : [2,3],
    "valor" : 1,
    "estado" : True
}

peon_blanco_4 = {
    "nombre" : "peon",
    "posicion" : [2,4],
    "valor" : 1,
    "estado" : True
}

peon_blanco_5 = {
    "nombre" : "peon",
    "posicion" : [2,5],
    "valor" : 1,
    "estado" : True
}

peon_blanco_6 = {
    "nombre" : "peon",
    "posicion" : [2,6],
    "valor" : 1,
    "estado" : True
}

peon_blanco_7 = {
    "nombre" : "peon",
    "posicion" : [2,7],
    "valor" : 1,
    "estado" : True
}

peon_blanco_8 = {
    "nombre" : "peon",
    "posicion" : [2,8],
    "valor" : 1,
    "estado" : True
}

#Piezas negra, posiciones, estado y valor

rey_negro = {
    "nombre" : "Rey",
    "fila" : [8,5],
    "valor" : "Demasiado",
    "estado" : True,
    "Jaque" : False
}

dama_negra = {
    "nombre" : "Dama",
    "fila" : [8,4],
    "valor" : 9,
    "estado" : True
}

alfil_negro_1 = {
    "nombre" : "Alfil",
    "posicion" : [8,3],
    "valor" : 3,
    "estado" : True
}

alfil_negro_2 = {
    "nombre" : "Alfil",
    "posicion" : [8,6],
    "valor" : 3,
    "estado" : True
}

caballo_negro_1 = {
    "nombre" : "Caballo",
    "posicion" : [8,2],
    "valor" : 5,
    "estado" : True
}

caballo_negro_2 = {
    "nombre" : "Caballo",
    "posicion" : [8,7],
    "valor" : 5,
    "estado" : True
}

torre_negra_1 = {
    "nombre" : "Torre",
    "posicion" : [8,1],
    "valor" : 5,
    "estado" : True
}

torre_negra_2 = {
    "nombre" : "Torre",
    "posicion" : [8,8],
    "valor" : 5,
    "estado" : True
}

peon_negro_1 = {
    "nombre" : "peon",
    "posicion" : [7,1],
    "valor" : 1,
    "estado" : True
}

peon_negro_2 = {
    "nombre" : "peon",
    "posicion" : [7,2],
    "valor" : 1,
    "estado" : True
}

peon_negro_3 = {
    "nombre" : "peon",
    "posicion" : [7,3],
    "valor" : 1,
    "estado" : True
}

peon_negro_4 = {
    "nombre" : "peon",
    "posicion" : [7,4],
    "valor" : 1,
    "estado" : True
}

peon_negro_5 = {
    "nombre" : "peon",
    "posicion" : [7,5],
    "valor" : 1,
    "estado" : True
}

peon_negro_6 = {
    "nombre" : "peon",
    "posicion" : [7,6],
    "valor" : 1,
    "estado" : True
}

peon_negro_7 = {
    "nombre" : "peon",
    "posicion" : [7,7],
    "valor" : 1,
    "estado" : True
}

peon_negro_8 = {
    "nombre" : "peon",
    "posicion" : [7,8],
    "valor" : 1,
    "estado" : True
}
