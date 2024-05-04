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
                porcentaje_anual_rendimiento = int(datos_cuentas[6])
                unaCuenta = Cuenta(apellido, nombre, DNI, telefono, saldo_cuenta, CVU_cuenta, porcentaje_anual_rendimiento)
                self.__arreglo_cuentas = np.append(self.__arreglo_cuentas, np.array(unaCuenta))

    def ObtenerCantidadDeCuentas(self) -> int:
        return len(self.__arreglo_cuentas)

    def actualizarSaldo(self, cuenta_arreglo, importe_transaccion) -> None:
        self.__arreglo_cuentas[cuenta_arreglo].setSaldoCuenta(importe_transaccion)

    def mostrarDatosDeLaCuenta(self, cuenta_arreglo):
        print(self.__arreglo_cuentas[cuenta_arreglo])

    def verificarDNIDelCliente(self, dni_ingresado, gestor_transacciones) -> None:
        cantidad_cuentas = int(self.ObtenerCantidadDeCuentas())
        cuenta_arreglo:int = 0
        dni_encontrado:bool = False
        while cuenta_arreglo < cantidad_cuentas and dni_encontrado != True:
            dni_arreglo = str(self.__arreglo_cuentas[cuenta_arreglo].getDNICuenta())
            if dni_ingresado == dni_arreglo:
                CVU_arreglo = str(self.__arreglo_cuentas[cuenta_arreglo].getCVUCuenta())
                gestor_transacciones.verificarTransaccionDelCliente(CVU_arreglo, cuenta_arreglo, self)
                self.mostrarDatosDeLaCuenta(cuenta_arreglo)
                dni_encontrado = True
            cuenta_arreglo += 1

    def mostrar(self) -> None:
        for i in range(len(self.__arreglo_cuentas)):
            print(self.__arreglo_cuentas[i])