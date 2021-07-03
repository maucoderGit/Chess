def game():
    pass

def turnos(player):
    if player == 0:
        return 0
    else:
        return 1

# def tablero(): 

#     columna_a = [1,2,3,4,5,6,7,8]
#     columna_b = [1,2,3,4,5,6,7,8]
#     columna_c = [1,2,3,4,5,6,7,8]
#     columna_d = [1,2,3,4,5,6,7,8]
#     columna_e = [1,2,3,4,5,6,7,8]
#     columna_f = [1,2,3,4,5,6,7,8]
#     columna_g = [1,2,3,4,5,6,7,8]
#     columna_h = [1,2,3,4,5,6,7,8]

#Programando nuestro tablero de ajedrez

def run():
    player = 0
    if player == 0:
        print ("Juegan blancas.")
        player += 1
    else:
        print ("Juegan negras")
        player -= 1


if __name__ == "__main__":
    run()