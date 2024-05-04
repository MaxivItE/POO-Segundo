from GestorMotos import GestorMotos
from GestorPedidos import GestorPedidos
from Pedido import Pedido
from os import system

def marcarOpcion() -> str:
    print("\n                ***RAPIPEDIDO***")
    print (" 1. Crear nuevo Pedido")
    print (" 2. Cambiar tiempo de entrega Real de un Pedido")
    print (" 3. Mostrar datos del Conductor")
    print (" 4. Mostrar el pago de comisión para cada conductor")
    print (" 0. Salir")
    return input (" Respuesta: ")
    

def verificarPatenteIngresada(patente_ingresada: str) -> str:
    patente_encontrada: bool = gestor_motos.verificarPatente(patente_ingresada)
    while patente_encontrada != True:
        system("cls")
        print (" Error al ingresar la patente, la moto no existe. Por favor ingrese una patente correcta\n ")
        patente_ingresada: str = input ("Patente de la moto asignada al pedido: ")
        patente_encontrada = gestor_motos.verificarPatente(patente_ingresada)
    return patente_ingresada

def cargarPedidos() -> None:
    patente_moto_ingresada: str = (input ("Patente de la moto asignada al pedido: "))
    patente_moto_ingresada = verificarPatenteIngresada(patente_moto_ingresada)
    id_pedido_ingresado: str = (input ("Identificador del Pedido: "))
    comidas_pedidas_ingresadas: str = (input ("Comidas a llevar: "))
    tiempo_entrega_ingresado: int = (input ("Tiempo Estimado de entrega (En minutos): "))
    tiempo_real_ingresado: int = (input("Tiempo Real de entrega: "))
    precio_pedido_ingresado: float = (input("Precio del pedido: ")) 
    unNuevoPedido = Pedido(patente_moto_ingresada, id_pedido_ingresado, comidas_pedidas_ingresadas, tiempo_entrega_ingresado, tiempo_real_ingresado, precio_pedido_ingresado)
    gestor_pedidos.agregarPedido(unNuevoPedido)

def modificarTiempoRealEntrega() -> None:
    patente_moto_ingresada: str = input("Número de Patente: ")
    patente_moto_ingresada = verificarPatenteIngresada(patente_moto_ingresada)
    id_pedido_ingresado: str = input("Identificador de Pedido: ")
    tiempo_real_ingresado: int = input("Tiempo real de entrega: ")
    gestor_pedidos.buscarPedidosPatente(patente_moto_ingresada, id_pedido_ingresado, tiempo_real_ingresado)

def mostrarDatosDelConductor() -> None:
    patente_moto_ingresada: str = input ("Número de Patente de moto: ")
    patente_moto_ingresada = verificarPatenteIngresada(patente_moto_ingresada)
    gestor_motos.buscarDatosDeConductor(patente_moto_ingresada)
    gestor_pedidos.buscarTiempoRealEntrega(patente_moto_ingresada)

def mostrarPagoDeComisiones() -> None:
    gestor_motos.listarMotos(gestor_pedidos)

def menuOpciones() -> None:
    opcion: str = marcarOpcion()
    while opcion != '0':
        system("cls")
        match opcion.lower():
            case '1': cargarPedidos()
            case '2': modificarTiempoRealEntrega()
            case '3': mostrarDatosDelConductor()
            case '4': mostrarPagoDeComisiones()
            case 'mostrar': 
                gestor_motos.mostrarListaMotos()
                gestor_pedidos.mostrarListaPedidos()
        opcion = marcarOpcion()

def menu() -> None:
    system("cls")
    menuOpciones()

if __name__ == '__main__':
    gestor_motos = GestorMotos()
    gestor_pedidos = GestorPedidos()
    gestor_pedidos.ordenarPedidos()
    menu()