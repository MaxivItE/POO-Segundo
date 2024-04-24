from CajadeAhorro import CajadeAhorro
from manejadorCajadeAhorro import manejadorCajadeAhorro
from test import test

if __name__ == '__main__':
    caja_de_ahorro = CajadeAhorro
    manejador_clase_ahorro = manejadorCajadeAhorro()
    test(caja_de_ahorro, manejador_clase_ahorro)