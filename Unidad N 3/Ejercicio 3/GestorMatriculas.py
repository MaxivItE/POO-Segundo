from ClaseMatricula import Matricula

class GestorMatriculas:
    __lista_matriculas: list

    def __init__(self) -> None:
        self.__lista_matriculas = []

    def cargarMatricula(self, fecha_matricula, empleado, programa) -> None:
        matricula = Matricula(fecha_matricula, empleado, programa)
        self.__lista_matriculas.append(matricula)

    def mostrarDuracionMatriculaEmpleado(self, programa):
        nombre_programa = programa.getNombrePrograma()
        duracion_programa = programa.getDuracionPrograma()
        print(f"\n {nombre_programa}\n Duración: {duracion_programa} días")

    def verificarMatriculasEmpleado(self, id_ingresado) -> None:
        cantidad_matriculas = int(len(self.__lista_matriculas))
        contador_matriculas:int = 0
        print("\n---MATRICULAS DEL EMPLEADO---")
        for pos_matricula in range(cantidad_matriculas):
            empleado_lista = self.__lista_matriculas[pos_matricula].getEmpleado()
            id_empleado = int(empleado_lista.getIDEmpleado())
            if id_ingresado == id_empleado:
                programa_lista = self.__lista_matriculas[pos_matricula].getPrograma()
                self.mostrarDuracionMatriculaEmpleado(programa_lista)
                contador_matriculas += 1
        if contador_matriculas == 0:
            print("\n El empleado NO está matriculado a ningun programa de capacitación")

    def verificarEmpleadosPrograma(self, nombre_programa) -> None:
        cantidad_matriculas = len(self.__lista_matriculas)
        contador_empleados:int = 0
        print(f"\n---MATRICULADOS AL PROGRAMA DE CAPACITACION {nombre_programa.upper()}---")
        for pos_matricula in range(cantidad_matriculas):
            programa_lista = self.__lista_matriculas[pos_matricula].getPrograma()
            nombre_programa_lista = programa_lista.getNombrePrograma()
            if nombre_programa.lower() == nombre_programa_lista.lower():
                contador_empleados += 1
                empleado_lista = self.__lista_matriculas[pos_matricula].getEmpleado()
                print(empleado_lista)
        if contador_empleados == 0:
            print(f"\n El programa de Capacitacion {nombre_programa_lista} NO tiene empleados matriculados")

    def verificarMatriculacionEmpleado(self, id_empleado) -> bool:
        pos_matricula: int = 0
        cantidad_matriculas = len(self.__lista_matriculas)
        while pos_matricula < cantidad_matriculas:
            empleado_lista = self.__lista_matriculas[pos_matricula].getEmpleado()
            id_empleado_lista = int(empleado_lista.getIDEmpleado())
            if id_empleado == id_empleado_lista:
                return True
            pos_matricula += 1
        return False

    def mostrarMatriculas(self) -> None:
        print("\n---MOSTRAR MATRICULAS DE EMPLEADOS---")
        for pos_matricula in range(len(self.__lista_matriculas)):
            print(self.__lista_matriculas[pos_matricula])