from GestorMotos import GestorMotos
from GestorPedidos import GestorPedidos
from Pedido import Pedido
from os import system

def verificarPatenteIngresada(patente_ingresada: str):
    patente_encontrada: bool = gestor_motos.verificarPatente(patente_ingresada)
    while patente_encontrada != True:
        system("cls")
        print (" Error al ingresar la patente, la moto no existe. Por favor ingrese una patente correcta\n ")
        patente_ingresada = (input ("Patente de la moto asignada al pedido: "))
        patente_encontrada = gestor_motos.verificarPatente(patente_ingresada)

def cargarPedidos():
    patente_moto_ingresada: str = (input ("Patente de la moto asignada al pedido: "))
    verificarPatenteIngresada(patente_moto_ingresada)
    id_pedido_ingresada: str = (input ("Identificador del Pedido: "))
    comidas_pedidas_ingresadas: str = (input ("Comidas a llevar: "))
    tiempo_entrega_ingresado: int = (input ("Tiempo Estimado de entrega (En minutos): "))
    tiempo_real_ingresado: float = (input("Tiempo Real de entrega: "))
    precio_pedido_ingresado: float = (input("Precio del pedido: ")) 
    unNuevoPedido = Pedido(patente_moto_ingresada, id_pedido_ingresada, comidas_pedidas_ingresadas, tiempo_entrega_ingresado, tiempo_real_ingresado, precio_pedido_ingresado)
    gestor_pedidos.agregarPedido(unNuevoPedido)


def marcarOpcion() -> str:
    print (" 1. Crear nuevo Pedido")
    print (" 0. Salir")
    opcion = str (input (" Respuesta: "))
    return opcion

def menuOpciones() -> None:
    opcion: str = marcarOpcion()
    while opcion != '0':
        system("cls")
        match opcion:
            case '1':
                cargarPedidos()
            
            case 'mostrar':
                    gestor_motos.mostrarListaMotos()
                    gestor_pedidos.mostrarListaPedidos()
        opcion = marcarOpcion()

def menu() -> None:
    menuOpciones()

if __name__ == '__main__':
    system("cls")
    gestor_motos = GestorMotos()
    gestor_pedidos = GestorPedidos()
    menu()