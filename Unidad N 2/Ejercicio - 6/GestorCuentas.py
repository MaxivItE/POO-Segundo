from Cuenta import Cuenta
import numpy as np
import csv

class GestorCuentas:
    __arreglo_cuentas = np.zeros(0, object)

    def __init__(self) -> None:
        self.inicializarArregloDeCuentas()

    def inicializarArregloDeCuentas(self) -> None:
        with open("cuentasBilletera.csv", 'r') as archivo_cuentas:
            cuenta = csv.reader(archivo_cuentas, delimiter=',')
            next(cuenta)
            print("\n")
            for datos_cuentas in cuenta:
                apellido = str(datos_cuentas[0])
                nombre = str(datos_cuentas[1])
                DNI = str(datos_cuentas[2])
                telefono = str(datos_cuentas[3])
                saldo_cuenta = float(datos_cuentas[4])
                CVU_cuenta = str(datos_cuentas[5])
                unaCuenta = Cuenta(apellido, nombre, DNI, telefono, saldo_cuenta, CVU_cuenta)
                self.__arreglo_cuentas = np.append(self.__arreglo_cuentas, np.array(unaCuenta))

    def obtenerCantidadDeCuentas(self) -> int:
        return len(self.__arreglo_cuentas)

    def buscarSaldoActual(self, cuenta_arreglo):    
        saldo_cuenta:float = 0
        cuenta_archivo:int = 0
        with open("cuentasBilletera.csv", 'r') as archivo_cuentas:
            cuenta = csv.reader(archivo_cuentas, delimiter=',')
            next(cuenta)
            print("\n")
            for datos_cuenta in cuenta:
                if cuenta_arreglo == cuenta_archivo:
                    saldo_cuenta = float(datos_cuenta[4])
                    return saldo_cuenta
                cuenta_archivo += 1

    def actualizarSaldo(self, cuenta_arreglo, transacciones_total) -> None:
        saldo_cuenta = float(self.buscarSaldoActual(cuenta_arreglo))
        saldo_cuenta += transacciones_total
        self.__arreglo_cuentas[cuenta_arreglo].setSaldoCuenta(saldo_cuenta)

    def mostrarDatosDeLaCuenta(self, cuenta_arreglo):
        print(self.__arreglo_cuentas[cuenta_arreglo])

    def mostrarErrorDeBusqueda(self, dato_no_encontrado) -> None:
        print(f"\n\t Error al buscar {dato_no_encontrado} del cliente. {dato_no_encontrado} No existe\n")

    def buscarDNIDelCliente(self, dni_ingresado):
        cuenta_arreglo:int = 0
        cantidad_cuentas = int(self.obtenerCantidadDeCuentas())
        while cuenta_arreglo < cantidad_cuentas:
            dni_arreglo = str(self.__arreglo_cuentas[cuenta_arreglo].getDNICuenta())
            if dni_ingresado == dni_arreglo:
                return str(cuenta_arreglo)
            cuenta_arreglo += 1
        return "No existe"

    def verificarDNIDelCliente(self, dni_ingresado, gestor_transacciones) -> None:
        dni_encontrado = str(self.buscarDNIDelCliente(dni_ingresado))
        if dni_encontrado == "No existe":
            self.mostrarErrorDeBusqueda("El Documento")
        else:
            CVU_arreglo = str(self.__arreglo_cuentas[int(dni_encontrado)].getCVUCuenta())
            gestor_transacciones.verificarTransaccionDelCliente(CVU_arreglo, int(dni_encontrado), self)
            self.mostrarDatosDeLaCuenta(int(dni_encontrado))

    def modificarPorcentajeAnualDeRendimiento(self, nuevo_porcentaje_anual_rendimiento) -> None:
        Cuenta.setPorcentajeAnualRendimiento(nuevo_porcentaje_anual_rendimiento)
        print("\n\t Porcentaje Anual de Rendimiento actualizado.\n")

    def actualizarSalarioDeLosClientes(self) -> None:
        cantidad_cuentas = int(self.obtenerCantidadDeCuentas())
        for cuenta_arreglo in range(cantidad_cuentas):
            self.__arreglo_cuentas[cuenta_arreglo].updateSaldoCuenta()
        print("\t Saldos de los Clientes actualizados.\n")

    def buscarCVUDelCliente(self, CVU_ingresado) -> bool:
        cantidad_cuentas = int(self.obtenerCantidadDeCuentas())
        cuenta_arreglo:int = 0
        while cuenta_arreglo < cantidad_cuentas:
            CVU_arreglo = str(self.__arreglo_cuentas[cuenta_arreglo].getCVUCuenta())
            if CVU_ingresado == CVU_arreglo:
                return str(cuenta_arreglo)
            cuenta_arreglo += 1
        return "No existe"

    def mostrarSaldoDelCliente(self, CVU_cliente) -> None:
        saldo_cliente = float(self.__arreglo_cuentas[CVU_cliente].getSaldoCliente())
        print("\n Saldo Actual: ${:.2f}" .format(saldo_cliente))

    def verificarCVUDelCliente(self, CVU_ingresado, gestor_transacciones) -> None:
        CVU_encontrado = str(self.buscarCVUDelCliente(CVU_ingresado))
        if CVU_encontrado == "No existe":
            self.mostrarErrorDeBusqueda("EL CVU")
        else:
            self.mostrarSaldoDelCliente(int(CVU_encontrado))
            gestor_transacciones.verificarTransaccionDelCliente(CVU_ingresado, int(CVU_encontrado), self)
            self.mostrarSaldoDelCliente(int(CVU_encontrado))

    def mostrar(self) -> None:
        porcentaje_anual_rendimiento = int(Cuenta.getPorcentajeAnualRendimiento())
        print("\n***CLIENTES DE LA EMPRESA: PAGO TUS CUENTAS***")
        for i in range(len(self.__arreglo_cuentas)):
            print(self.__arreglo_cuentas[i])
        print(f"\n Porcentaje Anual por Rendimiento para cada Cuenta: {porcentaje_anual_rendimiento}%\n")