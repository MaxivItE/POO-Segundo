from GestorMamas import GestorMadre
from GestorNacimientos import GestorNacimientos
from ClaseMenu import menu

if __name__ == '__main__':
    gestor_mamas = GestorMadre()
    gestor_nacimientos = GestorNacimientos()
    menu(gestor_mamas, gestor_nacimientos)