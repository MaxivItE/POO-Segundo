from Cliente import Cliente
import csv

class GestorClientes:
    __clientes: list = []

    def __init__(self) -> None:
        self.cargarListaDeClientes()

    def cargarListaDeClientes(self) -> None:
        with open("ClientesAbril2024.csv", 'r') as archivo_clientes:
            cliente = csv.reader(archivo_clientes, delimiter = ';')
            next(cliente)
            print("\n")
            for datos_cliente in cliente:
                nombre = str(datos_cliente[0])
                apellido = str(datos_cliente[1])
                DNI = str(datos_cliente[2])
                numero_tarjeta = str(datos_cliente[3])
                saldo_anterior = float(datos_cliente[4])
                unCliente = Cliente(nombre, apellido, DNI, numero_tarjeta, saldo_anterior)
                self.__clientes.append(unCliente)

    def mostrar(self) -> None:
        for i in range(len(self.__clientes)):
            print(self.__clientes[i])

