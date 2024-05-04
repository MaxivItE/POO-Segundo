from GestorCuentas import GestorCuentas
from GestorTransacciones import GestorTransacciones





def ingresarOpcion():
    print("a. Mostrar datos del Cliente")
    return str(input("Respuesta: "))

def ingresarDNIDelCliente():
    dni_ingresado = str(input(" Documento: "))
    gestor_cuentas.verificarDNIDelCliente(dni_ingresado, gestor_transacciones)
def menu():
    opcion = str(ingresarOpcion())
    match opcion:
        case 'a': ingresarDNIDelCliente()


if __name__ == '__main__':
    gestor_cuentas = GestorCuentas()
    #gestor_cuentas.mostrar()
    gestor_transacciones = GestorTransacciones()
    #gestor_transacciones.mostrar()
    menu()
    