import random

class Logica:
    def __init__(self):
        self.tablero=[]
        pass
    
    def iniciarTablero(self, n):
        for i in range(0,n):
            self.tablero.append([])
            for j in range (0,n):
                self.tablero[i].append(" ")
        return self.tablero
    
    def agregarMinas(self):
        for bomba in range(0,6):
            terminar= False
            while not terminar:
                nAleto1=random.randint(0,2)
                nAleto2=random.randint(0,2)
                if not (self.tablero[nAleto1][nAleto2]=="Boom"):
                    self.tablero [nAleto1][nAleto2]=="Boom"
                    terminar= True
        return self.tablero
        