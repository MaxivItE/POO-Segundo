import numpy as np
from os import system

def gestorVentas():
    sucursales: int = 5
    dias: int = 7
    farmacia = np.full((sucursales, dias), float(0))
    return farmacia

def menuOpciones():
    sucursales: int = 5-1
    dias: int = 7-1
    farmacia = gestorVentas()
    print("a) Ingresar Importe")
    print("b) Mostrar facturación de una Sucursal")
    print("c) Informar Sucursal más facturada por día")
    print("d) Obtener Sucursal menos facturada por semana")
    print("e) Mostrar total facturado de todas las sucursales")
    print("f) Salir")
    opcion=str(input("Respuesta: "))
    while opcion != 'f':
        system("cls")
        match opcion:
            case 'a':
                sucursal_casoA = int(input("Sucursal: "))
                dia_casoA = int(input("Dia: "))
                importe = float(input("Importe: "))
                if sucursal_casoA >5 or dia_casoA >7:
                    print("Error")
                else:
                    farmacia[sucursal_casoA-1][dia_casoA-1]+=importe
                    print(farmacia)

            case 'b':
                sucursal_casoB = int(input("Sucursal: "))
                sucursal_casoB-=1
                importe_total: float = 0
                for dia in range(len(farmacia[sucursales])):
                    importe_total += farmacia[sucursal_casoB][dia]
                print(f"\n Total de facturación de la Sucursal {sucursal_casoB+1}: ${importe_total}\n")

            case 'c':
                dia_casoC = int(input("Día: "))
                importe_maximo: float = 0
                sucursal_maxima: int = 0
                for sucursal in range(len(farmacia)):
                    importe_farmacia = farmacia[sucursal][dia_casoC-1]
                    if importe_farmacia > importe_maximo:
                        importe_maximo = importe_farmacia
                        sucursal_maxima = sucursal+1
                if importe_maximo == 0:
                    print(f"\n Ninguna farmacia facturó este día.\n")
                else:
                    print(f"\n La Sucursal {sucursal_maxima} es la que más facturo en el día {dia_casoC}: ${importe_maximo}\n")

            case 'd':
                importe_minimo: float = 9999999999999
                sucursal_menos: int = 0
                importe_farmacia: int = 0
                for sucursal in range(len(farmacia)):
                    for dia in range(len(farmacia[sucursal])):
                        importe_farmacia+=farmacia[sucursal][dia]
                    if importe_farmacia < importe_minimo:
                        importe_minimo = importe_farmacia
                        sucursal_menos = sucursal
                print(f"\n La Sucursal {sucursal_menos+1} es la que menos facturo en la semana: ${importe_minimo}\n")

            case 'e':
                importe_total: float = 0
                for sucursal in range(len(farmacia)):
                    for dia in range(len(farmacia[sucursal])):
                        importe_total+=farmacia[sucursal][dia]
                print(f"\n Importe Total Facturado en todas las sucursales: ${importe_total}\n")    

            case 'm':
                print(" ***FARMACIA FARMACUID***")
                print(farmacia)
        
        print("a) Ingresar Importe")
        print("b) Mostrar facturación de una Sucursal")
        print("c) Informar Sucursal más facturada por un día")
        print("d) Obtener Sucursal menos facturada por semana")
        print("e) Mostrar total facturado de todas las sucursales")
        print("f) Salir")
        opcion=str(input("Respuesta: "))

if __name__ == '__main__':
    menuOpciones()



