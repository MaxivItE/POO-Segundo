from ClasePublicacion import Publicacion

class Libro(Publicacion):
    __nombre_autor: str
    __fecha_edicion: str
    __cantidad_paginas: int

    def __init__(self, titulo, categoria, precio_base, nombre_autor, fecha_edicion, cantidad_paginas) -> None:
        super().__init__(titulo, categoria, precio_base)
        self.__nombre_autor = nombre_autor
        self.__fecha_edicion = fecha_edicion
        self.__cantidad_paginas = cantidad_paginas

    def getFechaEdicion(self) -> str:
        return self.__fecha_edicion

    def obtenerImporteDePublicacion(self, unLibro) -> float:
        porcentaje_total:int = 100
        precio_base = float(unLibro.getPrecioBase())
        fecha_actual:int = 2024
        fecha_edicion = str(unLibro.getFechaEdicion())
        ano_antiguedad = int(fecha_actual - int(fecha_edicion[6:]))
        precio_importe = float((precio_base * ano_antiguedad) / porcentaje_total)
        return precio_base - precio_importe

    def __str__(self) -> str:
        return '{}\n Nombre Del Autor: {}\n Fecha de Edición: {}\n Cantidad de Páginas: {}' .format(super().mostrarPublicacion(), self.__nombre_autor, self.__fecha_edicion, self.__cantidad_paginas)