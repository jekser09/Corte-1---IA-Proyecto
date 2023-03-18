import nodo
import sys
class ASC():

    def __init__(self,inicial,final) -> None:
        self.nodoInicial=inicial
        self.nodoMeta=final
        self.abierto=[]
        self.cerrado=[]
        sys

    def pintar(self, tablero)->None:
        for i in tablero:print(i[0], " ", i[1], " ", i[2])

    def actualizarPesos(self, lista, pp)->list:
        for i in lista:i.peso = pp + i.prof + i.peso
        return lista

    def ordenarSucesor(self,lista):
        n = len(lista)
        for i in range(n-1): 
            for j in range(0, n-i-1): 
                if lista[j].peso > lista[j+1].peso :
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista

    def busqueda(self)->None:
        nodosGenerados=0
        self.abierto.append(nodo.Nodo(self.nodoInicial,None,0,'Inicio',0))
        actual=self.abierto[0]
        while len(self.abierto)>0 and actual.estado!=self.nodoMeta:
            actual=self.abierto.pop(0)
            print("Regla aplicada: ", actual.regla)
            print("Peso: ", actual.peso)
            self.pintar(actual.estado)
            if actual not in self.cerrado:
                self.cerrado.append(actual)
                sucesores=actual.hallarSucesores(actual,self.nodoMeta)
                sucesores=self.actualizarPesos(sucesores,actual.peso)
                metaInSucesores=False
                nSuc=len(sucesores)
                nodosGenerados+=nSuc
                for i in sucesores:
                    if i.estado==self.nodoMeta:
                        metaInSucesores=True
                        actual=i
                        print("Regla aplicada: ", actual.regla)
                        print("Peso: ", actual.peso)
                        self.pintar(actual.estado)
                if nSuc>0 and not metaInSucesores:
                    #sorted(sucesores,key=lambda x:x.peso)
                    sucesores=self.ordenarSucesor(sucesores)
                    self.abierto=sucesores+self.abierto
        print("---------------------------------")
        print("La cantidad de nodos generados es: ", nodosGenerados)
        if actual.estado==self.nodoMeta:
            print("Se ha encontrado la solucion y es: ")
            sol = []
            while actual.padre != None:
                sol.insert(0, actual)
                actual = actual.padre
            for i in range(len(sol)):
                print("Mover a ", sol[i].regla)
                self.pintar(sol[i].estado)
        else:print("No se encontro la solucion")
