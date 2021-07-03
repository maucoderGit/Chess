import tablero


def game():
    pass

def turnos(player):
    if player == 0:
        return 0
    else:
        return 1


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