class Ninja:
    def __init__(self, nombre, apellido, mascota, premio, comida_mascota) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.mascota = mascota
        self.premio = premio
        self.comida_mascota = comida_mascota

    def banar(self):
        self.mascota.sonido()
        return self

    def caminar(self):
        self.mascota.jugar()
        print('pasear a la mascota')
        return self
    def comer(self):
        self.mascota.comer()
        print('alimentar mascota')
        return self
