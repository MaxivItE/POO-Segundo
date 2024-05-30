
class GestorProgramasCapacitacion:
    __lista_programas: list

    def __init__(self) -> None:
        self.__lista_programas = []

    def cargarPrograma(self, unPrograma) -> None:
        self.__lista_programas.append(unPrograma)

    def verificarNombrePrograma(self, nombre_programa):
        pos_programa:int = 0
        cantidad_programas = int(len(self.__lista_programas))
        while pos_programa < cantidad_programas:
            nombre_programa_lista = str(self.__lista_programas[pos_programa].getNombrePrograma())
            if nombre_programa.lower() == nombre_programa_lista.lower():
                return True
            pos_programa += 1
        return False

    def mostrarProgramas(self) -> None:
        print("\n---MOSTRAR PROGRAMAS DE CAPACITACIÓN---")
        for pos_programa in range(len(self.__lista_programas)):
            print(self.__lista_programas[pos_programa])