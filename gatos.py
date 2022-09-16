
from mascota import Mascota
class Gato(Mascota):

    def __init__(self,name,golosinas,salud,energia,tamano):
        super().__init__(name,'gato', golosinas, salud, energia)
        self.tamano=tamano
    def porte (self):
        porte_mascota=input('Cuál es el tamaño de tu mascota?\n')
        print(f'el tamaño de tu mascota es :{porte_mascota}')
        peso=int(input('El peso es?'))
        if peso>10:
            print('tamaño grande')
        else:
            print('tamaño pequeño')