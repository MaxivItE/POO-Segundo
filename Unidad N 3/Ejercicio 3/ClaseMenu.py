from os import system


def ingresarOpcion() -> int:
    print("\n 1. Informar duración de los programas de un empleado")
    print(" 2. Mostrar empleados de un Programa de capacitación")
    print(" 3. Mostrar empleados que NO están matriculados")
    print(" 0. Salir")
    return str(input("Respuesta: "))

def verificarExistenciaEmpleado(gestor_empleados, id_ingresado, gestor_matriculas):
    empleado_encontrado = bool(gestor_empleados.verificarIDEmpleado(id_ingresado))
    if empleado_encontrado != True:
        print(f"\n El empleado con el Identificador {id_ingresado} NO existe")
    else:
        gestor_matriculas.verificarMatriculasEmpleado(id_ingresado)

def verificarExistenciaPrograma(gestor_programas, nombre_programa, gestor_matriculas):
    programa_encontrado = bool(gestor_programas.verificarNombrePrograma(nombre_programa))
    if programa_encontrado != True:
        print(f"\n El programa {nombre_programa} NO existe")
    else:
        gestor_matriculas.verificarEmpleadosPrograma(nombre_programa)
def menu(gestor_empleado, gestor_matriculas, gestor_programas):
    system("cls")
    opcion = str(ingresarOpcion())
    while opcion != '0':
        system("cls")
        match opcion.lower():
            case '1':
                id_ingresado = int(input("Identicación del empleado: "))
                verificarExistenciaEmpleado(gestor_empleado, id_ingresado, gestor_matriculas)
            case '2':
                nombre_programa = str(input("Nombre del programa: "))
                verificarExistenciaPrograma(gestor_programas, nombre_programa, gestor_matriculas)
            case '3':
                gestor_empleado.verificarEmpleadosMatriculados(gestor_matriculas)
            case 'mostrar':
                gestor_empleado.mostrarEmpleados()
                gestor_programas.mostrarProgramas()
                gestor_matriculas.mostrarMatriculas()
            case _:
                print(" ERROR. Ingrese alguna de las opciones especificadas")
        opcion = ingresarOpcion()
    system("cls")
    print("\n\t\t\t\t\t Fin de programa.")