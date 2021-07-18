import move
import piezas



def run():
    move.run()
    resultado = ""
    player = 0
    piezas.rey(0,0,False)

    # while resultado != "blancas" or resultado != "negras" or resultado != "tablas":
    #     if player == 0:
    #         print ("Juegan blancas.")
    #         player += 1
    #     else:
    #         print ("Juegan negras")
    #         player -= 1


if __name__ == "__main__":
    run()