from GestorDeEquipo import GestorDeEquipo
from GestorFecha import GestorFechaDeFutbol
from os import system

def opcionesMenu() -> str:
    print("\n a. Mostrar Tabla de Posición de un Equipo")
    print(" b. Mostrar Tabla de Posición de la Liguilla de Rawson")
    print(" c. Cargar Tabla de Posición en un archivo CSV")
    print(" 0. Salir")
    return input("Respuesta: ")

def ingresarNombreEquipo(gestor_equipo, gestor_fechas) -> None:
    nombre_equipo_ingresado = str(input("Nombre del Equipo: "))
    system("cls")
    gestor_equipo.buscarDatosDeEquipo(nombre_equipo_ingresado, gestor_fechas)

def menu() -> None:
    opcion = str(opcionesMenu())
    while opcion != '0':
        system("cls")
        match opcion.lower():
            case 'a':
                ingresarNombreEquipo(gestor_equipo, gestor_fechas)
            case 'b':
                gestor_equipo.mostrarTablaDePosiciones(gestor_fechas)
            case 'c':
                gestor_equipo.cargarTablaDePosicionesEnCSV()
        opcion = str(opcionesMenu())

if __name__ == '__main__':
    gestor_fechas = GestorFechaDeFutbol()
    gestor_equipo = GestorDeEquipo()
    gestor_equipo.actualizarDatosDeLosEquipos(gestor_fechas)
    gestor_equipo.ordenarTablaDePosiciones()
    menu()