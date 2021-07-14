import move


def game():
    run()


def run():
    move.run()
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