
class Cuenta:
    __apellido: str
    __nombre: str
    __DNI: str
    __telefono: str
    __saldo_cuenta: float
    __CVU_cuenta: str
    __porcentaje_anual_rendimiento: int = 68

    def __init__(self, apellido, nombre, DNI, telefono, saldo_cuenta, CVU_cuenta) -> None:
        self.__apellido = apellido
        self.__nombre = nombre
        self.__DNI = DNI
        self.__telefono = telefono
        self.__saldo_cuenta = saldo_cuenta
        self.__CVU_cuenta = CVU_cuenta
        self.__porcentaje_anual_rendimiento = float(self.updatePorcentajeDiarioRendimiento())

    def getApellidoCuenta(self) -> str:
        return self.__apellido

    def getNombreCuenta(self) -> str:
        return self.__nombre

    def getDNICuenta(self) -> str:
        return self.__DNI

    def getCVUCuenta(self) -> str:
        return self.__CVU_cuenta

    def getSaldoCliente(self) -> float:
        return self.__saldo_cuenta
    def setSaldoCuenta(self, saldo_cuenta) -> None:
        self.__saldo_cuenta = saldo_cuenta

    def getPorcentajeDiarioRendimiento(self) -> float:
        porcentaje_diario_rendimiento: float = (self.__saldo_cuenta / 100) * self.__porcentaje_anual_rendimiento
        return porcentaje_diario_rendimiento

    def updateSaldoCuenta(self):
        porcentaje_saldo_rendimiento = float(self.getPorcentajeDiarioRendimiento())
        self.__saldo_cuenta += porcentaje_saldo_rendimiento

    @classmethod
    def getPorcentajeAnualRendimiento(cls) -> int:
        return cls.__porcentaje_anual_rendimiento
    @classmethod
    def setPorcentajeAnualRendimiento(cls, nuevo_porcentaje_anual_rendimiento) -> None:
        cls.__porcentaje_anual_rendimiento = nuevo_porcentaje_anual_rendimiento

    def updatePorcentajeDiarioRendimiento(self) -> float:
        porcentaje_anual_rendimiento = self.getPorcentajeAnualRendimiento()
        return porcentaje_anual_rendimiento / 365
    
    def __str__(self) -> str:
        return '\n Apellido: {}\n Nombre: {}\n Documento: {}\n Teléfono: {}\n Saldo: ${:.2f}\n CVU: {}\n Porcentaje diario de Rendimineto: {:.2f}%' .format(self.__apellido, self.__nombre, self.__DNI, self.__telefono, self.__saldo_cuenta, self.__CVU_cuenta, self.__porcentaje_anual_rendimiento)
