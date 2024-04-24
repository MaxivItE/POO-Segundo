from os import system

def crearCuenta(CajadeAhorro, manejador_clase_ahorro):
    seguir = "SI"
    while seguir != "-1":
        print("***CREAR CUENTA***")
        nroCuenta = str(input("Número de Cuenta: "))
        cuil = str(input("CUIL: "))
        apellido = str(input("Apellido: "))
        nombre = str(input("Nombre: "))
        saldo = float(input("Saldo: $"))
        unaCuenta = CajadeAhorro(nroCuenta, cuil, apellido, nombre, saldo)
        manejador_clase_ahorro.inicializarListaCajadeAhorro(unaCuenta)
        seguir = str(input("Quiere crear otra cuenta? (SI - NO): "))
        if seguir == "NO":
            seguir = "-1"
        system("cls")
    manejador_clase_ahorro.mostrar()

def menu2(manejador_clase_ahorro, CajadeAhorro):
    crearCuenta(CajadeAhorro, manejador_clase_ahorro)
    CUIL = str(input("\nIngrese CUIL: "))
    manejador_clase_ahorro.obtenerDatos(CUIL)

def test(CajadeAhorro, manejador_clase_ahorro):
    caja_de_ahorro01 = CajadeAhorro(str(123), str(2042917830), str("Araujo"), str("Maximiliano"), float(130000))
    caja_de_ahorro02 = CajadeAhorro(str(50), str(27242349585), str("Fernández"), str("María Soledad"), float(300000))
    caja_de_ahorro03 = CajadeAhorro(str(12), str(20261597805), str("Garcia"), str("Javier"), float(2000000))
    manejador_clase_ahorro.inicializarListaCajadeAhorro(caja_de_ahorro01)
    manejador_clase_ahorro.inicializarListaCajadeAhorro(caja_de_ahorro02)
    manejador_clase_ahorro.inicializarListaCajadeAhorro(caja_de_ahorro03)
    menu2(manejador_clase_ahorro, CajadeAhorro)