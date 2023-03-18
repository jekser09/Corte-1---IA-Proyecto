from os import system
import BusqProfundidad
import BusqAAsterisco
import AscColina
import Archivos

#Johand Esteban Castro Rodriguez
#Sebastian Alberto Martinez Gomez

class Main():
    def __init__(self) -> None:
        self.def_Nodos()
        self.menu()

    def def_Nodos(self)->None:
        self.__ESTINICIAL=[]
        self.__ESTFINAL=[]
        aux=Archivos.File().traerNodos()
        for i in aux:
            if i[0].lower()=='inicial':
                for j in i[1].split(','):self.__ESTINICIAL.append(list(map(lambda x:int(x),j.split(' '))))
            elif i[0].lower()=='final':
                for j in i[1].split(','):self.__ESTFINAL.append(list(map(lambda x:int(x),j.split(' '))))
        self.__ESTINICIAL=tuple(self.__ESTINICIAL)
        self.__ESTFINAL=tuple(self.__ESTFINAL)

    def pintar(self,tablero)->None:
        for i in range(3):
            print(tablero[i][0], " ", tablero[i][1], " ", tablero[i][2])


    def menu(self)->None:
        con = True
        while con:
            try:
                print("----------------------------------")
                print("--------- MENU PRINCIPAL ---------")
                print("----------------------------------")
                print("Estado Inicial: ")
                self.pintar(self.__ESTINICIAL)
                print("Estado Final: ")
                self.pintar(self.__ESTFINAL)
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
                            self.__ESTINICIAL[i][j] = 0
                    for i in range(3):
                        for j in range(3):
                            print("Numero en posicion ", i, ",", j, ": ")
                            self.__ESTINICIAL[i][j] = int(input("-> "))
                            self.pintar(self.__ESTINICIAL)
                    system("cls")
                elif opc == 2:
                    for i in range(3):
                        for j in range(3):
                            self.__ESTFINAL[i][j] = 0
                    for i in range(3):
                        for j in range(3):
                            print("Numero en posicion ", i, ",", j, ": ")
                            self.__ESTFINAL[i][j] = int(input("-> "))
                            self.pintar(self.__ESTFINAL)
                    system("cls")
                elif opc == 3:
                    if self.__ESTINICIAL!=self.__ESTFINAL:
                        system("cls")
                        print("--- BUSQUEDA PROFUNDIDAD ---")
                        pro=int(input("Digite el nivel de profundidad: "))
                        x=BusqProfundidad.BPP(self.__ESTINICIAL,self.__ESTFINAL,pro)
                        x.busqueda()
                    else:
                        print("¡El estado inicial es igual al estado meta!")
                elif opc == 4:
                    if self.__ESTINICIAL!=self.__ESTFINAL:
                        system("cls")
                        print("--- ASCENSO COLINA ---")
                        AscColina.ASC(self.__ESTINICIAL,self.__ESTFINAL).busqueda()
                    else:
                        print("¡El estado inicial es igual al estado meta!")
                elif opc == 5:
                    if self.__ESTFINAL!=self.__ESTINICIAL:
                        system("cls")
                        print("--- A* ---")
                        z=BusqAAsterisco.AA(self.__ESTINICIAL,self.__ESTFINAL)
                        z.busqueda()
                    else:
                        print("¡El estado inicial es igual al estado meta!")
                elif opc == 6:
                    print(f'')
                elif opc == 0:
                    con = False
                else:
                    print("Opcion Incorrecta, intente de nuevo")
            except Exception as e:
                print(f"Error {e}, intente de nuevo")
        print("¡¡¡ APLICACION FINALIZADA !!!")

if __name__=='__main__':
    Main()
