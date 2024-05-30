from GestorMiembros import GestorMiembros
from GestorVisualizaciones import GestorVisualizaciones
from ClaseMenu import menu

if __name__ == "__main__":
    gestor_miembros = GestorMiembros()
    gestor_visualizaciones = GestorVisualizaciones()
    menu(gestor_miembros, gestor_visualizaciones)