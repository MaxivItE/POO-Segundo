
class manejadorCajadeAhorro:
    __lista_caja_ahorro = []

    def inicializarListaCajadeAhorro(self, unaCuenta):
        self.__lista_caja_ahorro.append(unaCuenta)

    def mostrarDatosEncontrados(self, encontrado, caja_ahorro):
        if encontrado == True:
            print(self.__lista_caja_ahorro[caja_ahorro])
        else:
            print(" CUIL No válido")

    def obtenerDatos(self, CUIL):
        i=0
        cantidad_caja_ahorro = len(self.__lista_caja_ahorro)
        encontrado = False
        while i<cantidad_caja_ahorro and encontrado != True:
            CUIL_lista = self.__lista_caja_ahorro[i].getCUIL()
            if CUIL_lista == CUIL:
                caja_ahorro = i
                encontrado = True
                self.mostrarDatosEncontrados(encontrado, caja_ahorro)
            i+=1

    def mostrar(self):
        for i in range(len(self.__lista_caja_ahorro)):
            print(self.__lista_caja_ahorro[i])