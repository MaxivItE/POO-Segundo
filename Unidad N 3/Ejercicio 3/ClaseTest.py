from ClaseEmpleado import Empleado
from ClaseProgramaCapacitacion import ProgramaCapacitacion

def test(gestor_empleados, gestor_programas, gestor_matriculas) -> None:
    empleado1 = Empleado("Mariano Ponce", 124, "Programador")
    empleado2 = Empleado("Alejandro Baez", 160, "Sistemas")
    empleado3 = Empleado("Mauricio Perez", 84, "Electrónico")
    programa1 = ProgramaCapacitacion("Liderazgo y Gestión de Conflictos en Organizaciones", 2, 120)
    programa2 = ProgramaCapacitacion("Curso de Inglés Orientado a la Atención al Turista", 5, 90)
    programa3 = ProgramaCapacitacion("Diplomatura en Paquete Adobe Multimedia", 3, 210)
    gestor_empleados.inscribirEmpleado(empleado1)
    gestor_empleados.inscribirEmpleado(empleado2)
    gestor_empleados.inscribirEmpleado(empleado3)
    gestor_programas.cargarPrograma(programa1)
    gestor_programas.cargarPrograma(programa2)
    gestor_programas.cargarPrograma(programa3)
    gestor_matriculas.cargarMatricula("27/05/2024", empleado3, programa1)
    gestor_matriculas.cargarMatricula("23/5/2024", empleado1, programa3)
    gestor_matriculas.cargarMatricula("29/05/2024", empleado2, programa3)