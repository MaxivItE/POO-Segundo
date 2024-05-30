from os import system

def ingresarOpcion() -> str:
    print("\n\t\t---MENU DEL SANATORIO EL CEREZO---")
    print(" a. Mostrar partos de Mamá")
    print(" b. Mostrar partos múltiples de Mamás")
    print(" 0. Salir")
    return input(str("Respuesta: "))

def menu(gestor_mamas, gestor_nacimientos) -> None:
    system("cls")
    opcion = str(ingresarOpcion())
    while opcion != '0':
        system("cls")
        match opcion.lower():
            case 'a':
                DNI_ingresado = input(str("Documento de Mama: "))
                gestor_mamas.verificarDNIMadre(DNI_ingresado, gestor_nacimientos)
            case 'b':
                gestor_mamas.verificarPartoMadre(gestor_nacimientos)
            case 'mostrar':
                gestor_mamas.mostrarMadres()
                gestor_nacimientos.mostrarNacimientos()
            case _:
                print("ERROR al ingresar la opción. Por favor, ingrese una de las opciones especificadas")
        opcion = ingresarOpcion()
    system("cls")
    print("\t\t\t\t  Fin de Programa.")