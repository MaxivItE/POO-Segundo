
class GestorEmpleados:
    __lista_empleados: list

    def __init__(self) -> None:
        self.__lista_empleados = []
    
    def inscribirEmpleado(self, unEmpleado) -> None:
        self.__lista_empleados.append(unEmpleado)

    def verificarIDEmpleado(self, id_ingresado) -> None:
        pos_empleado:int = 0
        cantidad_empleados = int(len(self.__lista_empleados))
        while pos_empleado < cantidad_empleados:
            id_empleado = int(self.__lista_empleados[pos_empleado].getIDEmpleado())
            if id_ingresado == id_empleado:
                return True
            pos_empleado += 1
        return False

    def verificarEmpleadosMatriculados(self, gestor_matriculas) -> None:
        cantidad_empleados = len(self.__lista_empleados)
        contador_sin_matriculacion:int = 0
        contador_con_matriculacion:int = 0
        print("\n---EMPLEADOS SIN MATRICULACIÓN---\n")
        for pos_empleado in range(cantidad_empleados):
            id_empleado = self.__lista_empleados[pos_empleado].getIDEmpleado()
            empleado_encontrado = bool(gestor_matriculas.verificarMatriculacionEmpleado(id_empleado))
            if empleado_encontrado != True:
                contador_sin_matriculacion += 1
                nombre_apellido_empleado = self.__lista_empleados[pos_empleado].getNombreApellido()
                print(f" El empleado {nombre_apellido_empleado} NO está matricado a ningún programa de capacitación")
            else:
                contador_con_matriculacion += 1
        if (contador_con_matriculacion == 0) or (cantidad_empleados == 0):
            print("\n NINGÚN empleado está matriculados en algun programa de capacitación")
        elif contador_sin_matriculacion == 0:
            print(" TODOS los empleados están matriculados en algun programa de capacitación")

    def mostrarEmpleados(self) -> None:
        print("\n---MOSTRAR EMPLEADOS---")
        for pos_empleado in range(len(self.__lista_empleados)):
            print(self.__lista_empleados[pos_empleado])