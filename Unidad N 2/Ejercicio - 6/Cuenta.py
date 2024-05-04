
class Cuenta:
    __apellido: str
    __nombre: str
    __DNI: str
    __telefono: str
    __saldo_cuenta: float
    __CVU_cuenta: str
    __porcentaje_anual_rendimiento: str

    def __init__(self, apellido, nombre, DNI, telefono, saldo_cuenta, CVU_cuenta, porcentaje_anual_rendimiento) -> None:
        self.__apellido = apellido
        self.__nombre = nombre
        self.__DNI = DNI
        self.__telefono = telefono
        self.__saldo_cuenta = saldo_cuenta
        self.__CVU_cuenta = CVU_cuenta
        self.__porcentaje_anual_rendimiento = porcentaje_anual_rendimiento
    
    def getDNICuenta(self) -> str:
        return self.__DNI
    
    def getCVUCuenta(self) -> str:
        return self.__CVU
    
    def setSaldoCuenta(self, importe_transaccion):
        self.__saldo_cuenta += importe_transaccion
    
    def __str__(self) -> str:
        return ' \n Apellido: {}\n Nombre: {}\n Documento: {}\n Teléfono: {}\n Saldo: {}\n CVU: {}\n Porcentaje anual de Rendimineto: {}' .format(self.__apellido, self.__nombre, self.__DNI, self.__telefono, self.__saldo_cuenta, self.__CVU_cuenta, self.__porcentaje_anual_rendimiento)
