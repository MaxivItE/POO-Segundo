import csv

def funcion():
    try:
        archivo = open("datos.csv")
        reader = csv.reader(archivo,delimiter=';')
        for f in reader:
            print(f[0], f[1])
    except IndexError:
        print("Error al procesar los datos")
    except FileNotFoundError:
        print("Error en el archivo")
    else:
        print("Sin excepciones")
    finally:
        print("Se terminó")

if __name__ == '__main__':
    funcion()

'''
*Si el archivo tiene los siguientes datos se produce la excpeción?          ["Error al procesar los datos" y "Se terminó"]
*Si no puede abrir el archivo "datos.csv" ¿que mensaje/s muestra?           ["Error en el archivo" y "Se terminó"]
*¿Si no encuentra el archivo "datos.csv" se produce la excepción?           ["Error en el archivo" y "Se terminó"]
*Si no se produce ninguna excepción, ¿qué mensaje/s muestra?                ["Sin excepciones" y "Se terminó"]
'''