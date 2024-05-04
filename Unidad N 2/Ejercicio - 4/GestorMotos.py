from Moto import Moto
import csv

class GestorMotos:
    __lista_motos: list = []

    def __init__(self) -> None:
        self.inicializarListaMotos()
    
    def inicializarListaMotos(self) -> None:
        with open("datosMotos.csv", 'r') as archivo_motos:
            reader = csv.reader(archivo_motos, delimiter=',')
            next(reader)
            print("\n")
            for fila in reader:
                patente: str = fila[0]
                marca: str = fila[1]
                nombre_conductor: str = fila[2]
                apellido_conductor: str = fila[3]
                kilometraje: float = fila[4]
                unaMoto = Moto(patente, marca, nombre_conductor, apellido_conductor, kilometraje)
                self.__lista_motos.append(unaMoto)
        archivo_motos.close()
    
    def obtenerTamanoLista(self) -> int:
        return len(self.__lista_motos)
    
    def verificarPatente(self, patente_ingresada: str) -> bool:
        tamano_lista_motos: int = self.obtenerTamanoLista()
        patente_encontrada: bool = False
        i: int = 0
        while (i < tamano_lista_motos) and (patente_encontrada != True):
            patente_lista: str = self.__lista_motos[i].getPatente()
            if patente_ingresada == patente_lista:
                patente_ingresada = patente_lista
                return True
            i+=1
        return patente_encontrada

    def mostrarConductor(self, posicion_patente_lista):
        print(self.__lista_motos[posicion_patente_lista])

    def buscarDatosDeConductor(self, patente_moto_ingresada) -> None:
        tamano_lista_motos: int = self.obtenerTamanoLista()
        patente_encontrada: bool = False
        i: int = 0
        while (i < tamano_lista_motos) and (patente_encontrada != True):
            patente_lista: str = self.__lista_motos[i].getPatente()
            if patente_moto_ingresada == patente_lista:
                posicion_patente_lista = i
            i+=1
        self.mostrarConductor(posicion_patente_lista)
    
    def mostrarListaMotos(self, moto, patente_moto_lista):
        nombre_conductor_lista = self.__lista_motos[moto].getNombreConductor()
        apellido_conductor_lista = self.__lista_motos[moto].getApellidoConductor()
        print(f"\n Patente de Moto: {patente_moto_lista}")
        print(f" Conductor: {apellido_conductor_lista} {nombre_conductor_lista}")

    def listarMotos(self, gestor_pedidos):
        tamano_lista_motos: int = self.obtenerTamanoLista()
        for i in range(tamano_lista_motos):
            lista_id_pedidos: str = []
            lista_id_tiempo_estimado: str = []
            lista_tiempo_real: str = []
            lista_precio: float = []
            precio_total: float = 0
            comision: int = 0
            patente_moto_lista = self.__lista_motos[i].getPatente()
            self.mostrarListaMotos(i, patente_moto_lista)
            gestor_pedidos.listarPedidosMotos(patente_moto_lista, lista_id_pedidos, lista_id_tiempo_estimado, lista_tiempo_real, lista_precio)
            print(" Identificador de pedido     Tiempo estimado     Tiempo real     Precio")
            tamano_id_pedidos_lista = len(lista_id_pedidos)
            for j in range(tamano_id_pedidos_lista):
                print(f" {lista_id_pedidos[j]}\t\t\t     {lista_id_tiempo_estimado[j]} minutos          {lista_tiempo_real[j]} minutos\t$ {lista_precio[j]}")
            tamano_precio_lista = len(lista_precio)
            for k in range(tamano_precio_lista):
                precio_total+=float(lista_precio[k])
            print(f" Total: ${precio_total}")
            comision = precio_total*0.2
            print(f" Comisión: ${comision} (20% del total)")
            print(f"-------------------------------------------------------------------------------------------------------")

    def mostrar(self) -> None:
        tamano_lista_motos = self.obtenerTamanoLista()
        for i in range(tamano_lista_motos):
            print(self.__lista_motos[i])