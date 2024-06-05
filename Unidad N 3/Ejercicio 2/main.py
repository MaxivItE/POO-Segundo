from GestorLadrillos import GestorLadrillos
from GestorMateriales import GestorMateriales
from ClaseTest import test
from ClaseMenu import menu

if __name__ == '__main__':
    gestor_ladrillos = GestorLadrillos()
    gestor_materiales = GestorMateriales()
    test(gestor_ladrillos, gestor_materiales)
    menu(gestor_ladrillos, gestor_materiales)