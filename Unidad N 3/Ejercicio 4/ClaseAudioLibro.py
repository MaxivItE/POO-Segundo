from ClasePublicacion import Publicacion

class AudioLibro(Publicacion):
    __tiempo_reproduccion: int
    __nombre_narrador: str

    def __init__(self, titulo, categoria, precio_base, tiempo_reproduccion, nombre_narrador) -> None:
        super().__init__(titulo, categoria, precio_base)
        self.__tiempo_reproduccion = tiempo_reproduccion
        self.__nombre_narrador = nombre_narrador

    def obtenerImporteDePublicacion(self, unAudioLibro) -> float:
        precio_base = float(unAudioLibro.getPrecioBase())
        porcentaje_regalias:int = 10
        porcentaje_total: int = 100
        precio_importe = float((precio_base * porcentaje_regalias) / porcentaje_total)
        return precio_base + precio_importe

    def __str__(self) -> str:
        return '{}\n Tiempo de Reproducción: {} minutos\n Nombre del narrador/a: {}' .format(super().mostrarPublicacion(), self.__tiempo_reproduccion, self.__nombre_narrador)