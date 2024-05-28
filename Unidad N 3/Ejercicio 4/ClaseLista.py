from ClaseNodo import Nodo

class Lista:
    __comienzo_publicacion: Nodo
    __actual_publicacion: Nodo
    __indice_actual: int
    __tope_lista: int

    def __init__(self) -> None:
        self.__comienzo_publicacion = None
        self.__actual_publicacion = None
        self.__indice_actual = 0
        self.__tope_lista = 0

    def __iter__(self):
        return self

    def __next__(self) -> object:
        if self.__indice_actual == self.__tope_lista:
            self.__actual_publicacion = self.__comienzo_publicacion
            self.__indice_actual = 0
            raise StopIteration
        else:
            self.__indice_actual += 1
            dato_publicacion = self.__actual_publicacion.getDatoPublicacion()
            self.__actual_publicacion = self.__actual_publicacion.getSiguientePublicacion()
            return dato_publicacion

    def agregarPublicacion(self, unaPublicacion) -> None:
        nodo = Nodo(unaPublicacion)
        nodo.setSiguientePublicacion(self.__comienzo_publicacion)
        self.__comienzo_publicacion = nodo
        self.__actual_publicacion = nodo
        self.__tope_lista += 1

    def mostrarTipoDePublicacion(self, pos_lista, Libro, AudioLibro) -> None:
        publicacion_acutal = self.__comienzo_publicacion
        publicacion_encontrada:bool = False
        while not publicacion_encontrada and publicacion_acutal != None:
            dato_publicacion = publicacion_acutal.getDatoPublicacion()
            if pos_lista == self.__indice_actual:
                if isinstance(dato_publicacion, Libro):
                    publicacion_encontrada = True
                    print(f"\n La publicación {pos_lista + 1} en la Editorial es un libro")
                elif isinstance(dato_publicacion, AudioLibro):
                    publicacion_encontrada = True
                    print(f"\n La publicación {pos_lista + 1} en la Editorial es un Audio-Libro en CD")
            else:
                publicacion_acutal = publicacion_acutal.getSiguientePublicacion()
                self.__indice_actual += 1
        self.__indice_actual = 0
        if not publicacion_encontrada:
            print("ERROR. La posición buscada excede a la cantidad de publicaciones de la editorial.")

    def mostrarCantidadDePublicaciones(self, Libro, AudioLibro) -> None:
        contador_libros:int = 0
        contador_CDs:int = 0
        publicacion_actual = self.__comienzo_publicacion
        while publicacion_actual != None:
            dato_publicacion = publicacion_actual.getDatoPublicacion()
            if isinstance(dato_publicacion, Libro):
                contador_libros += 1
            elif isinstance(dato_publicacion, AudioLibro):
                contador_CDs += 1
            publicacion_actual = publicacion_actual.getSiguientePublicacion()
        print(f"\n Cantidad de Libros En La Editorial: {contador_libros}\n Cantidad de Audio-Libros en CDs de la Editorial: {contador_CDs}")

    def mostrarPublicaciones(self) -> None:
        print("\n ---PUBLICACIONES DE LA EDITORIAL---")
        publicacion_actual = self.__comienzo_publicacion
        while publicacion_actual != None:
            print(publicacion_actual)
            publicacion_actual = publicacion_actual.getSiguientePublicacion()