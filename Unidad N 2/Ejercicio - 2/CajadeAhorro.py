
class CajadeAhorro:
    def __init__(self, nroCuenta, cuil, apellido, nombre, saldo):
        self.__nroCuenta = nroCuenta
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__saldo = saldo

    def getCUIL(self):
        return self.__cuil

    def __str__(self):
        return '\n Número de Cuenta: {}\n Cuil: {}\n Apellido: {}\n Nombre: {}\n Saldo: ${}' .format(self.__nroCuenta, self.__cuil, self.__apellido, self.__nombre, self.__saldo)

    def extraer(self, importe=float):
        if self.__saldo >= importe:
            self.__saldo-=importe
            return self.__saldo
        else:
            return -1

    def depositar(self, importe):
        if importe > 0:
            self.__saldo+=importe
            return self.__saldo
        else:
            return -1

    def validarCUIL(self, cuilt):
        tamano_CUIL = 11
        tamano_CUIL_ingresado = len(cuilt)
        tipo_XY = cuilt[0:2]
        dni = cuilt[2:10]
        verificacion = cuilt[10:]
        if tamano_CUIL_ingresado == tamano_CUIL:
            hombre = 27
            mujer = 20
            tipo_XY = cuilt[0:2]
            dni = cuilt[2:10]
            verificacion = cuilt[10:11]
            codigo_verificacion = tipo_XY+dni
            multiplicador = 5
            sumador = 0
            for i in range(len(codigo_verificacion)):
                resultado = int(codigo_verificacion[i])*multiplicador
                sumador+=resultado
                multiplicador-=1
                if multiplicador < 2:
                    multiplicador=7
            resto = sumador % 11
            if resto == 0:
                verificacion = resto
            elif resto == 1:
                if tipo_sexo == hombre:
                    verificacion = 9
                elif tipo_sexo == mujer:
                    verificacion = 4
                tipo_sexo = 23
            else:
                verificacion = 11 - resto
            tipo_XY_verificado = str(input(" Tipo de XY (Hombre -> 20 - Mujer -> 27 - Empresa o Sociedad -> 30): "))
            cuilt_verificado = str(tipo_XY_verificado) + str(dni) + str(verificacion)
            if (str(cuilt) == cuilt_verificado):
                print (f"\n CUIL/T ingresado: {str(tipo_XY)}-{str(dni)}-{str(verificacion)}")
                return True
        else:
            if len(verificacion) == 0:
                verificacion = "Z"    
            print (f"\n El CUIL/T es erroneo\n CUIL/T ingresado: {str(tipo_XY)}-{str(dni)}-{str(verificacion)}\n CUIL/T Válido: XY-12345678-Z")
            return False