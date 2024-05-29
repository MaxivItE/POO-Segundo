
class Publicacion:
    __titulo: str
    __categoria: str
    __precio_base: float

    def __init__(self, titulo, categoria, precio_base) -> None:
        self.__titulo = titulo
        self.__categoria = categoria
        self.__precio_base = precio_base

    def getPrecioBase(self) -> float:
        return self.__precio_base

    def obtenerImporteDePublicacion(self) -> float:
        pass

    def cargarImporteDePublicacion(self) -> None:
        precio_final = float(self.obtenerImporteDePublicacion())
        self.__precio_base = precio_final

    def mostrarPublicacion(self) -> str:
        return '\n Título: {}\n Categoría: {}\n Precio Final: ${}' .format(self.__titulo, self.__categoria, self.__precio_base)