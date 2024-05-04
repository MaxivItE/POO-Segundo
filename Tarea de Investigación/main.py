from os import system
import numpy as np
class Persona:
    __nombre: str
    __edad: int
    
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def getNombre(self):
        return self.__nombre
    def getEdad(self):
        return self.__edad

    def __ne__(self, otraPersona):
        if self.__edad != otraPersona.__edad:
            return True
        else:
            return False

    def __gt__(self, otraPersona):
        if self.__edad > otraPersona.__edad:
            return True
        else:
            return False
        
    def __str__(self):
        return ' Nombre: {}\n Edad: {}' .format(self.__nombre, self.__edad) 
    
if __name__ == '__main__':
    system("cls")
    edades: np = np.full(3, object)
    persona_01 = Persona("Maxi", 23)
    persona_02 = Persona("Ludmila", 24)
    persona_03 = Persona("María", 49)
    edades[0] = persona_01
    edades[1] = persona_02
    edades[2] = persona_03
    i: int = 0
    edad = int(input("Ingrese Edad a buscar: "))
    persona_a_encontrar = Persona("Sin Nombre", edad)
    print(len(edades))
    
    persona_centinela = np.full(1, object)
    persona_centinela = persona_a_encontrar
    print(persona_centinela)
    np.concatenate([edades, [persona_centinela]])
    print(len(edades))
    for i in range(len(edades)):
        print(f" Nombre: {edades[i].getNombre()}")
        print(f" Edad: {edades[i].getEdad()}")
    '''while (edades[i]!=edad_centinela):
        print(edades[i])
        i+=1
    if i==len(edades):
        print(" El elemento no se encontró en el arreglo")
    else:
        print(f" El elemento se encontró en la posición {i+1}")'''
