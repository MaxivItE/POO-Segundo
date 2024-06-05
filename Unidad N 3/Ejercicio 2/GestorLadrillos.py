
class GestorLadrillos:
    __lista_ladrillos: list

    def __init__(self) -> None:
        self.__lista_ladrillos = []

    def agregarPedido(self, pedido_ladrillos) -> None:
        self.__lista_ladrillos.append(pedido_ladrillos)

    def verificarIDLadrillo(self, id_ladrillo_ingresado) -> int:
        posicion_ladrillo:int = 0
        cantidad_ladrillos = len(self.__lista_ladrillos)
        while posicion_ladrillo < cantidad_ladrillos:
            ladrillo = self.__lista_ladrillos[posicion_ladrillo].getLadrillo()
            id_ladrillo_buscado = int(ladrillo.getIDLadrillo())
            if id_ladrillo_ingresado == id_ladrillo_buscado:
                return posicion_ladrillo
            posicion_ladrillo += 1
        return -1

    def mostrarCostoCaracteristicasMaterial(self, ladrillo_encontrado, id_ladrillo_ingresado) -> None:
        material_ladrillo = self.__lista_ladrillos[ladrillo_encontrado].getMaterialRefractario()
        if material_ladrillo == None:
            print(f"\n El ladriilo de Identificador ({id_ladrillo_ingresado}) NO contiene material reciclado en su fabricación.")
        else:
            print(f"\n LADRILLO IDENTIFICADOR {id_ladrillo_ingresado}:")
            print(f"\n Material refractario: {material_ladrillo.getMaterial()}")
            print(f" Costo del material solicitado: ${material_ladrillo.getCostoAdicional()}")
            print(f" Caracteristicas: {material_ladrillo.getCaracteristicas()}")

    def obtenerCostoCaracteristicasMaterial(self, id_ladrillo_ingresado) -> None:
        ladrillo_encontrado = int(self.verificarIDLadrillo(id_ladrillo_ingresado))
        if ladrillo_encontrado == -1:
            print(f"\n El ladrillo de Identificador ({id_ladrillo_ingresado}) NO se encuentra en ningún pedido")
        else:
            self.mostrarCostoCaracteristicasMaterial(ladrillo_encontrado, id_ladrillo_ingresado)

    def mostrarCostoTotalPedido(self) -> None:
        cantidad_ladrillos = len(self.__lista_ladrillos)
        for posicion_ladrillo in range(cantidad_ladrillos):
            print(f"\n PEDIDO DE LADRILLOS NRO {posicion_ladrillo + 1}:")
            ladrillo = self.__lista_ladrillos[posicion_ladrillo].getLadrillo()
            material_ladrillo = self.__lista_ladrillos[posicion_ladrillo].getMaterialRefractario()
            costo_ladrillo = float(ladrillo.getCosto())
            cantidad_ladrillos = int(ladrillo.getCantidadLadrillo())
            costo_total = float(costo_ladrillo * cantidad_ladrillos)
            if material_ladrillo == None:
                print(f" Costo total: ${costo_total}")
            else:
                costo_adicional = material_ladrillo.getCostoAdicional()
                print(f" Costo total: ${costo_total + costo_adicional}")

    def mostrarDetallesFabricacion(self) -> None:
        cantidad_ladrillos = len(self.__lista_ladrillos)
        print("\n {:<10}\t{:<15}\t\t {:<10}" .format("Nº identificador", "Material", "Costo asociado"))
        for posicion_ladrillo in range(cantidad_ladrillos):
            ladrillo = self.__lista_ladrillos[posicion_ladrillo].getLadrillo()
            material_ladrillo = self.__lista_ladrillos[posicion_ladrillo].getMaterialRefractario()
            id_ladrillo = int(ladrillo.getIDLadrillo())
            costo_ladrillo = float(ladrillo.getCosto())
            cantidad_ladrillos = int(ladrillo.getCantidadLadrillo())
            if material_ladrillo == None:
                print(" {:<10}\t {:<15}\t ${:<10}" .format(id_ladrillo, "SIN MATERIAL REFRACTARIO", costo_ladrillo))
            else:
                nombre_material = str(material_ladrillo.getMaterial())
                costo_adicional = material_ladrillo.getCostoAdicional()
                print(" {:<10}\t\t{:<15}\t\t ${:<10}" .format(id_ladrillo, nombre_material, costo_ladrillo + costo_adicional))

    def mostrarListaPedidos(self) -> None:
        cantidad_ladrillos = len(self.__lista_ladrillos)
        print("\n---MOSTRAR LADRILLOS DE LA FABRICA 'NUESTRO HOGAR'---\n")
        for posicion_ladrillo in range(cantidad_ladrillos):
            self.__lista_ladrillos[posicion_ladrillo].mostrarPedidioLadrillos()