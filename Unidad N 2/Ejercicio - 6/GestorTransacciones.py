from Transaccion import Transaccion
import csv

class GestorTransacciones:
    __lista_transacciones: list = []

    def __init__(self) -> None:
        self.inicializarListaDeTransacciones()

    def verificarTipoDeTransaccion(self, tipo_transaccion) -> str:
        if tipo_transaccion == 'D' or tipo_transaccion == 'C':
            return 'Verificado'
        else:
            return 'Error'

    def inicializarListaDeTransacciones(self) -> None:
        with open("transaccionesBilletera.csv", 'r') as archivo_transacciones:
            transaccion = csv.reader(archivo_transacciones, delimiter=',')
            next(transaccion)
            print("\n")
            for datos_transaccion in transaccion:
                CVU_transaccion = str(datos_transaccion[0])
                numero_transaccion = str(datos_transaccion[1])
                importe_transaccion = float(datos_transaccion[2])
                verificacion_tipo_transicion = str(self.verificarTipoDeTransaccion(datos_transaccion[3]))
                if verificacion_tipo_transicion != 'Verificado':
                    print(f"\t Error al ingresar los datos de la transacción número: {numero_transaccion}. No se realizó la operación.\n")
                else:
                    tipo_transaccion = str(datos_transaccion[3])
                    unaTransaccion = Transaccion(CVU_transaccion, numero_transaccion, importe_transaccion, tipo_transaccion)
                    self.__lista_transacciones.append(unaTransaccion)

    def ObtenerCantidadDeTransacciones(self) -> int:
        return len(self.__lista_transacciones)

    def depositarImporte(self, transacciones_total, gestor_cliente, cuenta_arreglo) -> None:
        gestor_cliente.actualizarSaldo(cuenta_arreglo, transacciones_total)

    def verificarTransaccionDelCliente(self, CVU_cuenta, cuenta_arreglo, gestor_cliente):
        cantidad_transacciones = int(self.ObtenerCantidadDeTransacciones())
        transaccion_lista:int = 0
        transacciones_total:float = 0
        transacciones_encontradas:bool = False
        while transaccion_lista < cantidad_transacciones:
            CVU_transaccion = str(self.__lista_transacciones[transaccion_lista].getCVUTransaccion()) 
            if CVU_cuenta == CVU_transaccion:
                importe_transaccion = float(self.__lista_transacciones[transaccion_lista].getImporteTransaccion())
                transacciones_total += importe_transaccion
                transacciones_encontradas = True
            transaccion_lista += 1
        self.depositarImporte(transacciones_total, gestor_cliente, cuenta_arreglo)
        if transacciones_encontradas != True:
            print("\n\t No se encontraron transacciones")

    def mostrar(self) -> None:
        print("\n***TRANSACCIONES REALIZADAS***")
        for i in range(len(self.__lista_transacciones)):
            print(self.__lista_transacciones[i])