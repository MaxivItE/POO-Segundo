import csv

class Equipo:
    def __init__(self, id_equipo, nombre, goles_a_favor=0, goles_en_contra=0, diferencia_goles=0, puntos=0):
        self.id_equipo = id_equipo
        self.nombre = nombre
        self.goles_a_favor = goles_a_favor
        self.goles_en_contra = goles_en_contra
        self.diferencia_goles = diferencia_goles
        self.puntos = puntos

    def __gt__(self, other):
        if self.puntos != other.puntos:
            return self.puntos > other.puntos
        elif self.diferencia_goles != other.diferencia_goles:
            return self.diferencia_goles > other.diferencia_goles
        else:
            return self.goles_a_favor > other.goles_a_favor

class FechaFutbol:
    def __init__(self, fecha, id_equipo_local, id_equipo_visitante, goles_local, goles_visitante):
        self.fecha = fecha
        self.id_equipo_local = id_equipo_local
        self.id_equipo_visitante = id_equipo_visitante
        self.goles_local = goles_local
        self.goles_visitante = goles_visitante

class GestorEquipos:
    def __init__(self):
        self.equipos = []

    def cargar_equipos_desde_csv(self, archivo):
        with open(archivo, newline='' )as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                id_equipo, nombre = row
                self.equipos.append(Equipo(id_equipo, nombre))

    def mostrar_tabla_posiciones(self):
        print("Tabla de Posiciones:")
        print("{:<5} {:<30} {:<10} {:<10} {:<10} {:<10}".format("Pos.", "Equipo", "GF", "GC", "Dif. Gol", "Puntos"))
        for i, equipo in enumerate(sorted(self.equipos, reverse=True), start=1):
            print("{:<5} {:<30} {:<10} {:<10} {:<10} {:<10}".format(i, equipo.nombre, int(equipo.goles_a_favor), int(equipo.goles_en_contra), int(equipo.diferencia_goles), int(equipo.puntos)))
        print("-" * 65)

class GestorFechasFutbol:
    def __init__(self):
        self.fechas_futbol = []

    def cargar_fechas_futbol_desde_csv(self, archivo):
        with open(archivo, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                fecha, id_equipo_local, id_equipo_visitante, goles_local, goles_visitante = row
                self.fechas_futbol.append(FechaFutbol(fecha, id_equipo_local, id_equipo_visitante, int(goles_local), int(goles_visitante)))

    def actualizar_resultados(self, gestor_equipos):
        for fecha_futbol in self.fechas_futbol:
            equipo_local = next((equipo for equipo in gestor_equipos.equipos if equipo.id_equipo == fecha_futbol.id_equipo_local), None)
            equipo_visitante = next((equipo for equipo in gestor_equipos.equipos if equipo.id_equipo == fecha_futbol.id_equipo_visitante), None)
            if equipo_local and equipo_visitante:
                equipo_local.goles_a_favor += fecha_futbol.goles_local
                equipo_local.goles_en_contra += fecha_futbol.goles_visitante
                equipo_local.diferencia_goles = equipo_local.goles_a_favor - equipo_local.goles_en_contra
                equipo_visitante.goles_a_favor += fecha_futbol.goles_visitante
                equipo_visitante.goles_en_contra += fecha_futbol.goles_local
                equipo_visitante.diferencia_goles = equipo_visitante.goles_a_favor - equipo_visitante.goles_en_contra
                if fecha_futbol.goles_local > fecha_futbol.goles_visitante:
                    equipo_local.puntos += 3
                elif fecha_futbol.goles_local < fecha_futbol.goles_visitante:
                    equipo_visitante.puntos += 3
                else:
                    equipo_local.puntos += 1
                    equipo_visitante.puntos += 1

def cargar_equipos_desde_csv(gestor_equipos, archivo):
    gestor_equipos.cargar_equipos_desde_csv(archivo)

def cargar_fechas_futbol_desde_csv(gestor_fechas_futbol, archivo):
    gestor_fechas_futbol.cargar_fechas_futbol_desde_csv(archivo)

def mostrar_tabla_posiciones(gestor_equipos):
    gestor_equipos.mostrar_tabla_posiciones()

def actualizar_resultados(gestor_fechas_futbol, gestor_equipos):
    gestor_fechas_futbol.actualizar_resultados(gestor_equipos)

def almacenar_tabla_posiciones_en_csv(gestor_equipos, archivo):
    with open(archivo, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Equipo', 'Goles a Favor', 'Goles en Contra', 'Diferencia de Goles', 'Puntos'])
        for equipo in sorted(gestor_equipos.equipos, reverse=True):
            writer.writerow([equipo.nombre, equipo.goles_a_favor, equipo.goles_en_contra, equipo.diferencia_goles, equipo.puntos])

def main():
    gestor_equipos = GestorEquipos()
    gestor_fechas_futbol = GestorFechasFutbol()

    # Cargar datos desde archivos CSV
    cargar_equipos_desde_csv(gestor_equipos, "equipos2024.csv")
    cargar_fechas_futbol_desde_csv(gestor_fechas_futbol, "fechasFutbol.csv")

    while True:
        print("Menú de Opciones:")
        print("1. Mostrar Tabla de Posiciones")
        print("2. Actualizar Resultados")
        print("3. Almacenar Tabla de Posiciones en CSV")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_tabla_posiciones(gestor_equipos)
        elif opcion == '2':
            actualizar_resultados(gestor_fechas_futbol, gestor_equipos)
            print("Resultados actualizados correctamente.")
        elif opcion == '3':
            almacenar_tabla_posiciones_en_csv(gestor_equipos, "tabla_posiciones.csv")
            print("Tabla de posiciones almacenada en el archivo 'tabla_posiciones.csv'.")
        elif opcion == '4':
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()

