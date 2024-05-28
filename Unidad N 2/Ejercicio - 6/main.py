from GestorCuentas import GestorCuentas
from GestorTransacciones import GestorTransacciones
from os import system

def ingresarOpcion():
    print("\n a. Mostrar datos del Cliente con transacciones realizadas")
    print(" b. Actualizar porcentaje anual de Rendimiento de las Cuentas")
    print(" c. Actualizar el salario de los Clientes")
    print(" d. Mostrar saldo de Cliente con transacciones realizadas")
    print(" 0. Salir")
    return str(input("Respuesta: "))

def ingresarDNIDelCliente():
    dni_ingresado = str(input("Documento de la cuenta: "))
    gestor_cuentas.verificarDNIDelCliente(dni_ingresado, gestor_transacciones)

def ingresarPorcentajeAnualDeRendimiento() -> None:
    nuevo_porcentaje_anual_rendimiento = float(input("Nuevo Porcentaje Anual De Rendimiento: "))
    gestor_cuentas.modificarPorcentajeAnualDeRendimiento(nuevo_porcentaje_anual_rendimiento)

def ingresarCVUDelCliente() -> None:
    CVU_ingresado = str(input("CVU del Cliente: "))
    gestor_cuentas.verificarCVUDelCliente(CVU_ingresado, gestor_transacciones)

def menu():
    opcion = str(ingresarOpcion())
    while opcion != '0':
        system("cls")
        match opcion.lower():
            case 'a': ingresarDNIDelCliente()
            case 'b': ingresarPorcentajeAnualDeRendimiento()
            case 'c': gestor_cuentas.actualizarSalarioDeLosClientes()
            case 'd': ingresarCVUDelCliente()
            case 'mostrar': gestor_transacciones.mostrar(), gestor_cuentas.mostrar()
            case _: print("\t Error al ingresar la respuesta. Por favor, ingresa una opción especificada\n")
        opcion = (ingresarOpcion())

if __name__ == '__main__':
    system("cls")
    gestor_cuentas = GestorCuentas()
    gestor_transacciones = GestorTransacciones()
    menu()