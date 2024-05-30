
class Vehiculo:
    __color: str
    __cantRuedas: int
    def __init__(self, c, ruedas):
        self.__color = c
        self.__cantRuedas = ruedas

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

'''class Patineta():
    __color: str
    __cantRuedas: int
    def __init__(self, c, ruedas):
        self.__color = c
        self.__cantRuedas = ruedas'''

class GestorVehiculos:
    __lista: list
    def __init__(self):
        self.__lista=[]
    def agregar(self, unObjeto):
        if isinstance(unObjeto, Vehiculo):
            self.__lista.append
        else:
            raise TypeError

def test1():
    gestorV=GestorVehiculos()
    '''unaPatineta=Patineta("Roja", 3)'''
    unAuto=Motorizado("Blanco", 4, 120, 1.4)
    try:
        gestorV.agregar(unAuto)
        '''gestorV.agregar(unaPatineta)'''
    except TypeError:
        print("Solo se permiten agregar Vehículos")
    else:
        print("Se ha agregado un nuevo Vehículo al Gestor")
    finally:
        print("Bloque try completado")

if __name__ == '__main__':
    test1()

'''
Al ser ejecutada, produce la siguiente salida:

Seleccione una o más de una:
☐ a. Solo se permite agregar Vehículos
☑ b. Se ha agregado un nuevo Vehículo al Gestor
☑ c. Bloque try completado
'''