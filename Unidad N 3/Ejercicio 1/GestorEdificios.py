from Edificio import Edificio
from Departamento import Departamento
import csv

class GestorEdificios:
    __lista_edificios:list = []

    def __init__(self) -> None:
        self.inicializarListaDeEdificios()
    
    def inicializarListaDeEdificios(self) -> None:
        with open('EdificioNorte.csv', 'r') as archivo_edificios:
            edificio = csv.reader(archivo_edificios, delimiter=';')
            next(edificio)
            print("\n")
            aux = int(0)
            for datos_archivo in edificio:
                if aux != datos_archivo[0]:
                    aux = datos_archivo[0]
                    unEdificio = Edificio(id_edificio = int(datos_archivo[0]), nombre_edificio = str(datos_archivo[1]), direccion = str(datos_archivo[2]), nombre_Empresa_constructora = str(datos_archivo[3]), cantidad_pisos = int(datos_archivo[4]), cantidad_departamentos = int(datos_archivo[5]))
                    self.__lista_edificios.append(unEdificio)
                else:
                    unDepartamento = Departamento(id_departamento = int(datos_archivo[1]), nombre_apellido_propietario = str(datos_archivo[2]), numero_piso = int(datos_archivo[3]), numero_departamento = int(datos_archivo[4]), cantidad_habitaciones = int(datos_archivo[5]), cantidad_banos = int(datos_archivo[6]), superficie_cubierta = float(datos_archivo[7]))
                    unEdificio.setDepartamento(unDepartamento)

    def obtenerCantidadDeEdificios(self) -> int: 
        return len(self.__lista_edificios)

    def verificarNombreDeEdificio(self, nombre_edificio_ingresado) -> int:
        posicion_edificio:int = 0
        cantidad_edificios = int(self.obtenerCantidadDeEdificios())
        while posicion_edificio < cantidad_edificios:
            nombre_edificio_lista = str(self.__lista_edificios[posicion_edificio].getNombreEdificio())
            if nombre_edificio_ingresado.lower() == nombre_edificio_lista.lower():
                return posicion_edificio
            posicion_edificio += 1
        return -1

    def obtenerPropietarioDeUnEdificio(self, posicion_edificio, lista_propietarios_edificio) -> list:
        departamentos = list(self.__lista_edificios[posicion_edificio].getDepartamento())
        for posicion_departamento in departamentos:
            nombre_propietario_lista = str(posicion_departamento.getNombrePropietario())
            lista_propietarios_edificio.append(nombre_propietario_lista)

    def mostrarPropietariosDelEdificio(self, lista_propietario_edificio, posicion_edificio) -> None:
        cantidad_propietario_edificio = int(len(lista_propietario_edificio))
        nombre_edificio = str(self.__lista_edificios[posicion_edificio].getNombreEdificio())
        print(f"\n ***APELLIDO Y NOMBRE DE LOS RESIDENTES DEL {nombre_edificio.upper()}***")
        for numero_propietario in range(cantidad_propietario_edificio):
            print(f" {lista_propietario_edificio[numero_propietario]}")

    def realizarOpcionUno(self, nombre_edificio_ingresado) -> None:
        posicion_edificio = int(self.verificarNombreDeEdificio(nombre_edificio_ingresado))
        if posicion_edificio == -1:
            return print(" No se encontró el edificio buscado")
        else:
            lista_propietarios_edificio:list = []
            self.obtenerPropietarioDeUnEdificio(posicion_edificio, lista_propietarios_edificio)
            self.mostrarPropietariosDelEdificio(lista_propietarios_edificio, posicion_edificio)

    def calcularSuperficieDeEdificio(self, posicion_edificio) -> float:
        departamentos = list(self.__lista_edificios[posicion_edificio].getDepartamento())
        contador_superficie:float = 0
        for posicion_departamento in departamentos:
            superficie_cubierta = float(posicion_departamento.getSuperficieCubierta())
            contador_superficie += superficie_cubierta
        return contador_superficie

    def mostrarSuperficieTotalCubierto(self, nombre_edificio, superficie_total_edificio) -> str:
        print(f"\n Superficie Total del {nombre_edificio}: {superficie_total_edificio} M")

    def realizarOpcionDos(self, nombre_edificio_ingresado) -> None:
        posicion_edificio = int(self.verificarNombreDeEdificio(nombre_edificio_ingresado))
        if posicion_edificio == -1:
            return print(" No se encontró el edificio buscado")
        else:
            superficio_total_edificio: float = 0
            superficio_total_edificio = (self.calcularSuperficieDeEdificio(posicion_edificio))
            nombre_edificio = str(self.__lista_edificios[posicion_edificio].getNombreEdificio())
            self.mostrarSuperficieTotalCubierto(nombre_edificio, superficio_total_edificio)

    def obtenerDepartamentoDePropietario(self, posicion_edificio, nombre_propietario, otroEdificio, lista_departamentos_propietario) -> None:
        departamentos = list(self.__lista_edificios[posicion_edificio].getDepartamento())
        for departamento in departamentos:
            nombre_lista = str(departamento.getNombrePropietario())
            if nombre_propietario == nombre_lista:
                otroEdificio.setDepartamento(departamento)
                lista_departamentos_propietario.append(otroEdificio)
        #print(otroEdificio.getMostrarDatosDepartamentosEdificio())

    def obtenerCantidadDepartamentos(self, nombre_propietario, lista_departamentos_propietario) -> None:
        cantidad_edificios = int(self.obtenerCantidadDeEdificios())
        #print(f"\n ***DEPARTAMENTOS DEL PROPIETARIO {nombre_propietario.upper()}***")
        for posicion_edificio in range(cantidad_edificios):
            nombre_edificio = str(self.__lista_edificios[posicion_edificio].getNombreEdificio())
            id_edificio = int(self.__lista_edificios[posicion_edificio].getIdEdificio())
            otroEdificio = Edificio(id_edificio=id_edificio, nombre_edificio=nombre_edificio, direccion='', nombre_Empresa_constructora='', cantidad_pisos=0, cantidad_departamentos=0)
            #print(f" {nombre_edificio}")
            self.obtenerDepartamentoDePropietario(posicion_edificio, nombre_propietario, otroEdificio, lista_departamentos_propietario)

    def obtenerEdificioDepartamento(self, lista_departamentos_propietario, lista_id_edificios) -> None:
        cantidad_edificios = int(self.obtenerCantidadDeEdificios())
        cantidad_departamentos = int(len(lista_departamentos_propietario))
        for posicion_edificio in range(cantidad_edificios):
            edificio_departamento: int = 0
            id_edificio = int(self.__lista_edificios[posicion_edificio].getIdEdificio())
            edificio_encontrado:bool = False
            while edificio_departamento < cantidad_departamentos and edificio_encontrado != True:
                id_edificio_departamento = int(lista_departamentos_propietario[edificio_departamento].getIdEdificio())
                if id_edificio_departamento == id_edificio:
                    edificio_encontrado = True
                edificio_departamento += 1
            if edificio_encontrado != False:
                lista_id_edificios.append(id_edificio)

    def calcularSuperficieDeDepartamentos(self, lista_departamentos_propietario, nombre_edificio) -> float:
        superficie_cubierta:float = 0
        for edifcio_departamento in range(len(lista_departamentos_propietario)):
            nombre_edificio_departamento = str(lista_departamentos_propietario[edifcio_departamento].getNombreEdificio())
            if nombre_edificio == nombre_edificio_departamento:
                posicion_departamento = edifcio_departamento
                nombre_edificio = nombre_edificio_departamento
                superficie_cubierta += (lista_departamentos_propietario[posicion_departamento].getSuperficieCubierta(0))
        return superficie_cubierta

    def obtenerPorcentajeDelTotal(self, superficie_cubierta, superficie_total_edificio) -> float:
        return (superficie_cubierta / superficie_total_edificio) * 100

    def obtenerPorcentajeDeDepartamentos(self, lista_departamentos_propietario, posicion_departamento) -> float:
        return float(lista_departamentos_propietario[posicion_departamento].getSuperficieCubierta(0))

    def mostrarPorcentajeDeDepartamento(self, nombre_edificio, nombre_propietario, porcentaje_departamento, superficie_total_edificio) -> None:
        print("\n En el {}, el departamento de {} representa el {:.2f}% del total de la superfice del edificio: {} M" .format(nombre_edificio, nombre_propietario, porcentaje_departamento, superficie_total_edificio)) 

    def verificarSuperficieCubiertaDeDepartamentos(self, cantidad_departamentos, lista_departamentos_propietario, nombre_propietario) -> None:
        lista_id_edificios: list = []
        posicion_edificio:int = 0
        posicion_departamento:int = 0
        self.obtenerEdificioDepartamento(lista_departamentos_propietario, lista_id_edificios)
        cantidad_edificios = len(lista_id_edificios)
        if cantidad_edificios == 1:
            superficie_cubierta:float = 0
            nombre_edificio = str(self.__lista_edificios[posicion_edificio].getNombreEdificio())
            if cantidad_departamentos == 1:
                superficie_cubierta = float(self.obtenerPorcentajeDeDepartamentos(lista_departamentos_propietario, posicion_departamento))
            else:
                superficie_cubierta = self.calcularSuperficieDeDepartamentos(lista_departamentos_propietario, nombre_edificio)
            self.mostrarSuperficieTotalCubierto("Departamento", superficie_cubierta)
            superficie_total_edificio = float(self.calcularSuperficieDeEdificio(posicion_edificio))
            porcentaje_departamento = float(self.obtenerPorcentajeDelTotal(superficie_cubierta, superficie_total_edificio))
            self.mostrarPorcentajeDeDepartamento(nombre_edificio, nombre_propietario, porcentaje_departamento, superficie_total_edificio)
        elif cantidad_edificios > 1:
            for posicion_edificio in range(len(self.__lista_edificios)):
                nombre_edificio = str(self.__lista_edificios[posicion_edificio].getNombreEdificio())
                superficie_cubierta = float(self.calcularSuperficieDeDepartamentos(lista_departamentos_propietario, nombre_edificio))
                superficie_total_edificio = float(self.calcularSuperficieDeEdificio(posicion_edificio))
                porcentaje_departamento = float(self.obtenerPorcentajeDelTotal(superficie_cubierta, superficie_total_edificio))
                self.mostrarPorcentajeDeDepartamento(nombre_edificio, nombre_propietario, porcentaje_departamento, superficie_total_edificio)
        else:
            print(f" {nombre_propietario} No Tiene Departamentos en ningun Edificio.")

    def realizarOpcionTres(self, nombre_propietario) -> None:
        lista_departamentos_propietario: list = []
        self.obtenerCantidadDepartamentos(nombre_propietario, lista_departamentos_propietario)
        cantidad_departamentos = int(len(lista_departamentos_propietario))
        self.verificarSuperficieCubiertaDeDepartamentos(cantidad_departamentos, lista_departamentos_propietario, nombre_propietario)

    def mostrar(self) -> None:
        cantidad_edificios = int(self.obtenerCantidadDeEdificios())
        for numero_edificio in range(cantidad_edificios):
            print(self.__lista_edificios[numero_edificio].mostrarDatosEdificios())