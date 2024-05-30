from GestorEmpleados import GestorEmpleados
from GestorProgramasCapacitacion import GestorProgramasCapacitacion
from GestorMatriculas import GestorMatriculas
from ClaseTest import test
from ClaseMenu import menu

if __name__ == '__main__':
    gestor_empleados = GestorEmpleados()
    gestor_programas = GestorProgramasCapacitacion()
    gestor_matriculas = GestorMatriculas()
    test(gestor_empleados, gestor_programas, gestor_matriculas)
    menu(gestor_empleados, gestor_matriculas, gestor_programas)