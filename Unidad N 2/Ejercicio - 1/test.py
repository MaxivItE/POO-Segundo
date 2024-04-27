from os import system

def mostrarCajadeAhorro(caja_de_ahorro, i):
    print(f" Caja de Ahorro Nº{i+1}{caja_de_ahorro}\n-----------------")

def elegirCajadeAhorro(caja_de_ahorro01, caja_de_ahorro02, caja_de_ahorro03):
    system("cls")
    i: int = 0
    mostrarCajadeAhorro(caja_de_ahorro01, i)
    mostrarCajadeAhorro(caja_de_ahorro02, i+1)
    mostrarCajadeAhorro(caja_de_ahorro03, i+2)
    print("\n***ELEGIR CAJA DE AHORRO***")
    numero_caja_elegida = int(input(("\nCaja de Ahorro Nº: ")))
    match numero_caja_elegida:
        case 1: caja_ahorro_elegida = caja_de_ahorro01
        case 2: caja_ahorro_elegida = caja_de_ahorro02
        case 3: caja_ahorro_elegida = caja_de_ahorro03
    return caja_ahorro_elegida

def elegirOpcion():
    print("\n***CAJA DE AHORRO***\n")
    print(" 1. Extraer Plata")
    print(" 2. Depositar Ingreso")
    print(" 3. Validar mi CUIL/T")
    print(" 4. Cambiar Caja de Ahorro")
    print(" 0. Salir")
    opcion = int(input("Respuesta: "))
    return opcion

def extraerPlata(caja_ahorro_elegida):
    system("cls")
    importe_extraer = float(input("\nIngrese el importe a extraer: $"))
    caja_ahorro_elegida.extraer(importe_extraer)
    
def depositarIngresos(caja_ahorro_elegida):
    system("cls")
    importe_depositar = float(input("\nIngrese el importe a depositar: $"))
    caja_ahorro_elegida.depositar(importe_depositar)

def validarCUIL(caja_ahorro_elegida):
    cuilt = caja_ahorro_elegida.getCuil()
    validacion = caja_ahorro_elegida.validarCUIL(cuilt)
    if validacion == True:
        print("\n El CUIL/T es Válido")
    else:
        print(f"\n El CUIL/T NO es correcto")

def menu(caja_de_ahorro01, caja_de_ahorro02, caja_de_ahorro03):
    caja_ahorro_elegida = elegirCajadeAhorro(caja_de_ahorro01, caja_de_ahorro02, caja_de_ahorro03)
    opcion = elegirOpcion()
    while opcion != 0:
        match opcion:
            case 1: extraerPlata(caja_ahorro_elegida)
            case 2: depositarIngresos(caja_ahorro_elegida)
            case 3: validarCUIL(caja_ahorro_elegida)
            case 4: caja_ahorro_elegida = elegirCajadeAhorro(caja_de_ahorro01, caja_de_ahorro02, caja_de_ahorro03)
        print(caja_ahorro_elegida)
        opcion = elegirOpcion()

def test(CajadeAhorro):
    caja_de_ahorro01 = CajadeAhorro(str(123), str(20429178305), str("Araujo"), str("Maximiliano"), float(130000))
    caja_de_ahorro02 = CajadeAhorro(str(50), str(27242349585), str("Fernández"), str("María Soledad"), float(300000))
    caja_de_ahorro03 = CajadeAhorro(str(12), str(202615978050), str("Garcia"), str("Javier"), float(2000000))
    menu(caja_de_ahorro01, caja_de_ahorro02, caja_de_ahorro03)