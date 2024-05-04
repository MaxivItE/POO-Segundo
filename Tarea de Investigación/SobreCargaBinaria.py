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
    for i in range(len(edades)):
        print(f" Nombre: {edades[i].getNombre()}")
        print(f" Edad: {edades[i].getEdad()}")
    edad_binaria: np = np.full(1, object)
    edad = int(input("Ingrese Edad a buscar: "))
    persona_a_encontrar: object = Persona ("Sin Nombre", edad)
    edad_binaria = persona_a_encontrar
    inf: int = 0
    sup: int = len(edades)-1
    medio: int = (inf+sup)//2
    while ((inf<=sup) and (edades[medio]!=edad_binaria)):
        if (edades[medio]>edad_binaria):
            sup=medio-1
        else:
            inf=medio+1
        medio=(inf+sup)//2
    if (inf<=sup):
        print(f" El elemento se encuentra en la posición {medio+1}")
    else:
        print(" El emenento no se encontró")