import tablero
import piezas


def game():
    pass

def turnos(player):
    if player == 0:
        return 0
    else:
        return 1

def run():
    resultado = ""
    player = 0

    while resultado != "blancas" or resultado != "negras" or resultado != "tablas":
        if player == 0:
            print ("Juegan blancas.")
            player += 1
        else:
            print ("Juegan negras")
            player -= 1


if __name__ == "__main__":
    run()