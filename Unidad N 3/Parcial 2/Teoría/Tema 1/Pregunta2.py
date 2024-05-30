from abc import ABC
import abc

class Vehiculo(ABC):
    __color: str
    __cantRuedas: int
    def __init__(self, c, ruedas):
        self.__color = c
        self.__cantRuedas = ruedas
    @abc.abstractmethod
    def arrancar(self):
        pass
    def mostrarVehiculo(self):
        print("{}, {}, {}" .format(str(type(self)), self.__color, self.__cantRuedas))

class Motorizado(Vehiculo):
    __velocidadMaxima: int
    __cilindradas: float
    def __init__(self, c, ruedas, v, cil):
        super().__init__(c, ruedas)
        self.__velocidadMaxima = v
        self.__cilindradas = cil

class Camioneta(Motorizado):
    __capacidadDeCarrga: float
    def __init__(self, c, ruedas, v, cill, cap):
        super().__init__(c, ruedas, v, cill)
        self.__capacidadDeCarrga = cap

class Bicicleta(Vehiculo):
    __tipo: str
    def __init__(self, c, ruedas, tipo):
        super().__init__(c, ruedas)
        self.__tipo = tipo

def test():
    lista=[]
    unAuto=Motorizado("Blanco", 4, 120, 1.4)
    lista.append(unAuto)
    otroAuto=Motorizado("Rojo Rubí", 4, 170, 1.6)
    lista.append(otroAuto)
    unaBici=Bicicleta("Azul Marino", 2, "Urbana")
    lista.append(unaBici)
    otraBici=Bicicleta("Negra", 2, "Mountain Bike")
    lista.append(otraBici)
    unaCamioneta=Camioneta("Gris Perla", 4, 220, 1.9, 3000)
    lista.append(unaCamioneta)

if __name__ == '__main__':
    test()

'''
☐ a. No genera ningún error al ser ejecutada por el intérprete de Python 
☑ b. Genera un error al ser ejecutada por el intérprete de Python, porque todas las clases son abstractas.
'''