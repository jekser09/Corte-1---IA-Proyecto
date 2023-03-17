import Cromosoma as crom

class GEN():
    def __init__(self,inicial,final) -> None:
        self.nodoInicial=inicial
        self.nodoMeta=final
        self.poblacion=[]
    
    def pintar(self, tablero)->None:
        for i in tablero:print(i[0], " ", i[1], " ", i[2])
    
    def gen_Poblacion(self)->None:
        #cromosoma=nodo.Nodo()
        pass

    def busqueda(self)->None:
        cantGeneraciones=0
        actual=crom.crom(self.nodoInicial,None,0,'Inicial',0)
        self.poblacion=actual.hallarSucesores(actual,self.nodoMeta)
        

    
