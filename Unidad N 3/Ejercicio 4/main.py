from GestorPublicaciones import GestorPublicaciones
from GestorTest import test
from GestorMenu import menu

if __name__ == '__main__':
    gestor_publicaciones = GestorPublicaciones()
    test(gestor_publicaciones)
    menu(gestor_publicaciones)