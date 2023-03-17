from os import system
import BusqProfundidad
import BusqAAsterisco
import AscColina

estadoInicial = ([1, 2, 3], [0, 5, 6], [4, 7, 8])

estadoFinal = ([1, 2, 3], [4, 5, 6], [7, 8, 0])


def pintar(tablero):
    for i in range(3):
        print(tablero[i][0], " ", tablero[i][1], " ", tablero[i][2])


def menu():
    con = True
    while con:
        ##try:
            print("----------------------------------")
            print("--------- MENU PRINCIPAL ---------")
            print("----------------------------------")
            print("Estado Inicial: ")
            pintar(estadoInicial)
            print("Estado Final: ")
            pintar(estadoFinal)
            print("1: Cambiar Estado Inicial")
            print("2: Cambiar Estado Final")
            print("3: Busqueda por Profundidad")
            print("4: Ascenso Colina")
            print("5: A*")
            print("6: Algoritmo Genetico")
            print("0: Terminar")
            opc = int(input("Elija una opcion: "))
            if opc == 1:
                for i in range(3):
                    for j in range(3):
                        estadoInicial[i][j] = 0
                for i in range(3):
                    for j in range(3):
                        print("Numero en posicion ", i, ",", j, ": ")
                        estadoInicial[i][j] = int(input("-> "))
                        pintar(estadoInicial)
                system("cls")
            elif opc == 2:
                for i in range(3):
                    for j in range(3):
                        estadoFinal[i][j] = 0
                for i in range(3):
                    for j in range(3):
                        print("Numero en posicion ", i, ",", j, ": ")
                        estadoFinal[i][j] = int(input("-> "))
                        pintar(estadoFinal)
                system("cls")
            elif opc == 3:
                if estadoInicial!=estadoFinal:
                    system("cls")
                    print("--- BUSQUEDA PROFUNDIDAD ---")
                    pro=int(input("Digite el nivel de profundidad: "))
                    x=BusqProfundidad.BPP(estadoInicial,estadoFinal,pro)
                    x.busqueda()
                else:
                    print("¡El estado inicial es igual al estado meta!")
            elif opc == 4:
                if estadoInicial!=estadoFinal:
                    system("cls")
                    print("--- ASCENSO COLINA ---")
                    AscColina.ASC(estadoInicial,estadoFinal).busqueda()
                else:
                    print("¡El estado inicial es igual al estado meta!")
            elif opc == 5:
                if estadoInicial!=estadoFinal:
                    system("cls")
                    print("--- A* ---")
                    z=BusqAAsterisco.AA(estadoInicial,estadoFinal)
                    z.busqueda()
                else:
                    print("¡El estado inicial es igual al estado meta!")
            elif opc == 6:
                print(6)
            elif opc == 0:
                con = False
            else:
                print("Opcion Incorrecta, intente de nuevo")
        ##except:
            ##print("Opcion Incorrecta, intente de nuevo")
    print("¡¡¡ APLICACION FINALIZADA !!!")

    def pintar_Tabla(self,tabla)->None:
        for x in tabla:print(x)

menu()
