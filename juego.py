def turnos(player):
    if player == 0:
        return 0;
    else:
        return 0;

def tablero():

    fila_1 = ["a1","b1","c1","d1","e1","f1","g1","h1"]
    fila_2 = ["a2","b2","c2","d2","e2","f2","g2","h2"]
    fila_3 = ["a3","b3","c3","d3","e3","f3","g3","h3"]
    fila_4 = ["a4","b4","c4","d4","e4","f4","g4","h4"]
    fila_5 = ["a5","b5","c5","d5","e5","f5","g5","h5"]
    fila_6 = ["a6","b6","c6","d6","e6","f6","g6","h6"]
    fila_7 = ["a7","b7","c7","d7","e7","f7","g7","h7"]
    fila_8 = ["a8","b8","c8","d8","e8","f8","g8","h8"]
    
#Programando nuestro tablero de ajedrez

def run():
    player = 0;
    if player == 0:
        print ("Juegan blancas.")
        player += 1;
    else:
        print ("Juegan negras")
        player -= 1;


if __name__ == "__main__":
    run()