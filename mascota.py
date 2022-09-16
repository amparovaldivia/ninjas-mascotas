from http.client import GATEWAY_TIMEOUT
from msilib.schema import tables


class Mascota:
    def __init__(self, name, tipo, golosinas, salud, energia) -> None:
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = salud
        self.energia = energia

    def dormir(self):
        self.energia = self.energia+25
        return self

    def comer(self):
        self.energia = self.energia+5
        self.salud = self.salud+10
        return self

    def jugar(self):
        self.salud = self.salud+5
        return self

    def sonido(self):
        x=['gato','perro']
        

        if self.tipo == x[0]:
            print('miau')
        else:
            print('guau')
        return self    
    
                
