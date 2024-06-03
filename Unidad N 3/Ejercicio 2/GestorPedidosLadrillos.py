
class PedidoLadrillos:
    __ladrillo: object
    __material: object
    __numero_pedido:int = 0
    __cantidad_pedidos:int = 0
    
    def getLadrillo(self) -> object:
        return self.__ladrillo

    def getMaterialRefractario(self) -> object:
        return self.__material

    @classmethod
    def getCantidadPedidos(self) -> None:
        self.__cantidad_pedidos += 1

    @classmethod
    def getContadorPedidos(self) -> None:
        if self.__numero_pedido < self.__cantidad_pedidos:
            self.__numero_pedido += 1
        else:
            self.__numero_pedido = 1

    def agregarCostoAdicional(self) -> None:
        costo_adicional = float(self.__material.getCostoAdicional())
        self.__ladrillo.setCosto(costo_adicional)

    def __init__(self, ladrillo, material_refractario = None) -> None:
        self.getCantidadPedidos()
        self.__ladrillo = ladrillo
        if material_refractario != None:
            self.__material = material_refractario
        else:
            self.__material = None

    def mostrarPedidioLadrillos(self) -> None:
        self.getContadorPedidos()
        print(f"\n---PEDIDO NRO: {self.__numero_pedido}---")
        print(self.__ladrillo)
        if self.__material != None:
            print(self.__material)
            print(f"\n [Costo Final: {self.__ladrillo.getCosto() + self.__material.getCostoAdicional()}]")
        else:
            print("\n El ladriilo no contiene material reciclado en su fabricación.")