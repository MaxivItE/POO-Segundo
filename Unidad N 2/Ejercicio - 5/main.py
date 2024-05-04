from GestorDeEquipo import GestorDeEquipo
from GestorFecha import GestorFechaDeFutbol

def opcionesMenu() -> str:
    print("a. Mostrar Tabla de Posición de un Equipo")
    print("b. Mostrar Tabla de Posición de la Liguilla de Rawson")
    return input("Respuesta: ")

def ingresarNombreEquipo(gestor_de_equipo, gestor_fechas) -> None:
    nombre_equipo_ingresado = str(input("Nombre del Equipo: "))
    gestor_de_equipo.buscarDatosDeEquipo(nombre_equipo_ingresado, gestor_fechas)

def menu() -> None:
    gestor_fechas = GestorFechaDeFutbol()
    gestor_de_equipo = GestorDeEquipo()
   
    opcion = str(opcionesMenu())
    match opcion:
        case 'a':
            ingresarNombreEquipo(gestor_de_equipo, gestor_fechas)
        case 'b':
            gestor_de_equipo.actualizarDatosDeLosEquipos(gestor_fechas)
            gestor_de_equipo.ordenarTablaDePosiciones()
            gestor_de_equipo.mostrarTablaDePosiciones(gestor_fechas)

if __name__ == '__main__':
    menu()