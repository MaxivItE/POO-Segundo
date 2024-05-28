from ClasePublicacion import Publicacion

class GestorPublicaciones:
    __lista_publicaciones: list

    def __init__(self) -> None:
        self.__lista_publicaciones = []

    def cargarPublicacion(self, unaPublicacion) -> None:
        self.__lista_publicaciones.append(unaPublicacion)
        self.__lista_publicaciones[-1].cargarImporteDePublicacion(self.__lista_publicaciones[-1])

    def mostrarTipoDePublicacion(self, pos_lista, Libro, AudioLibro) -> None:
        pos_publicacion:int = 0
        publicacion_encontrdad:bool = False
        cantidad_publicaciones = int(len(self.__lista_publicaciones))
        while pos_publicacion < cantidad_publicaciones and publicacion_encontrdad != True:
            if isinstance(self.__lista_publicaciones[pos_lista-1], Libro):
                print(f"\n La publicación en la posicion {pos_lista} en la lista de publicaciones es un libro")
                publicacion_encontrdad = True
            elif isinstance(self.__lista_publicaciones[pos_lista-1], AudioLibro):
                print(f"\n La publicación en la posicion {pos_lista} de la lista de publicaciones es un Audio-libro en CD")
                publicacion_encontrdad = True
            pos_publicacion += 1

    def mostrarCantidadDePublicaciones(self, Libro, AudioLibro) -> None:
        contador_libros:int = 0
        contador_CDs:int = 0
        for pos_publicidad in range(len(self.__lista_publicaciones)):
            if isinstance(self.__lista_publicaciones[pos_publicidad], Libro):
                contador_libros += 1
            elif isinstance(self.__lista_publicaciones[pos_publicidad], AudioLibro):
                contador_CDs += 1
        print(f"\n Cantidad de Libros En La Editorial: {contador_libros}\n Cantidad de Audio-Libros en CDs de la Editorial: {contador_CDs}")

    def mostrarPublicaciones(self) -> None:
        print("\n ---PUBLICACIONES DE LA EDITORIAL---")
        for pos_publicacion in range(len(self.__lista_publicaciones)):
            print(self.__lista_publicaciones[pos_publicacion].mostrarPublicacion())

    def mostrar(self) -> None:
        for pos_publicacion in range(len(self.__lista_publicaciones)):
            print(self.__lista_publicaciones[pos_publicacion])