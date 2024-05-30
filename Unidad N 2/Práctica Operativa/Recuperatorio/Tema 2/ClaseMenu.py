from os import system

def ingresarOpcion() -> str:
    print("\n\t   ---MENU DE OPCIONES DE LA PLATAFORMA NETVIEW---")
    print(" 1 - Mostrar cantidad de Minutos vistos")
    print(" 2 - Mostrar Miembros que han realizado Visualizaciones simultaneas") 
    print(" 0. Salir")
    return str(input("Respuesta: "))

def menu (gestor_miembros, gestor_visualizaciones):
    system("cls")
    opcion = str(ingresarOpcion())
    while opcion != '0':
        system("cls")
        match opcion.lower():
            case '1':
                correo_ingresado = str(input("Correo Electrónico: "))
                gestor_miembros.verificarCorreoMiembro(correo_ingresado, gestor_visualizaciones)
            case '2':
                gestor_miembros.obtenerIDMiembro(gestor_visualizaciones)
            case 'mostrar':
                gestor_miembros.mostrarMiembros()
                gestor_visualizaciones.mostrarVisualizaciones()
            case _:
                print(" ERROR al ingresar la opción. Ingrese una de las especificaciones dadas")
        opcion = ingresarOpcion()
    system("cls")
    print("\t\t\t\t\t Fin del programa.")
