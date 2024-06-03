from os import system

def ingresarOpcion() -> str:
    print("\n---MENU DE LA FABRICA DE LADRILLOS 'NUESTRO HOGAR'---")
    print("\n 1. Mostrar costo y caracteristicas de pedido solicitado")
    print(" 2. Mostrar costo total de los ladrillos")
    print(" 3. Mostrar detalles asociados de la fabicación de ladrillos")
    print(" 0. Salir")
    return str(input("Respuesta: "))

def menu(gestor_ladrillos, gestor_materiales):
    system("cls")
    opcion = str(ingresarOpcion())
    while opcion != '0':
        system("cls")
        match opcion.lower():
            case '1':
                id_ladrillo = int(input("Identificador del ladrillo buscado: "))
                gestor_ladrillos.obtenerCostoCaracteristicasMaterial(id_ladrillo)
            case '2':
                gestor_ladrillos.mostrarCostoTotalPedido()
            case '3':
                gestor_ladrillos.mostrarDetallesFabricacion()
            case 'mostrar_ladrillos':
                gestor_ladrillos.mostrarListaPedidos()
            case 'mostrar_materiales':
                gestor_materiales.mostrarMaterialesRefractarios()
            case _:
                print(" ERROR al ingresar la opción. Por favor, ingrese una de las opciones especificadas")
        opcion = ingresarOpcion()
    system("cls")
    print("\n\t\t\t\t\t Fin de Programa.")
