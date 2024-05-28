from ClaseLibro import Libro
from ClaseAudioLibro import AudioLibro
from os import system

def ingresarOpcion() -> str:
    print("\n 1. Agregar Publicaciones a la Editorial")
    print(" 2. Mostrar un tipo de Publicación en específico")
    print(" 3. Mostrar cantidad de Publicaciones en la Editorial")
    print(" 4. Mostrar Publicaciones disponibles de la Editorial")
    print(" 0. Salir")
    return str(input("Respuesta: "))

def ingresarFormatoDePublicacion() -> str:
    print("1. Libros Impresos")
    print("2. Audio-Libros en CD")
    return str(input(">>> "))

def cargarDatosDePublicacion(tipo_formato) -> tuple:
    print(f"---LLENAR LOS DATOS DEL {tipo_formato.upper()}---")
    titulo_publicacion = str(input(f"\n Titulo del {tipo_formato}: "))
    categoria_publicacion = str(input(" Categoría: "))
    precio_publicacion = str(input(f" Precio Base del {tipo_formato}: "))
    return titulo_publicacion, categoria_publicacion, precio_publicacion

def cargarPublicacionDeLibro() -> tuple:
    nombre_autor = str(input(" Nombre del Autor: "))
    fecha_edicion = str(input(" Fecha de Edición: "))
    cantidad_paginas = int(input(" Cantidad de páginas: "))
    return nombre_autor, fecha_edicion, cantidad_paginas

def cargarPublicacionDeAudioLibro() -> tuple:
    tiempo_reproduccion = int(input(" Tiempo de Reproducción: "))
    nombre_narrador = str(input(" Nombre del Narrador: "))
    return tiempo_reproduccion, nombre_narrador

def agregarPublicacion(formato_publicacion, clase_lista):
    formato_encontrado:bool = False
    while formato_encontrado != True:
        system("cls")
        if formato_publicacion == '1':
            formato_libro = str("Libro")
            datos_publicacion = tuple(cargarDatosDePublicacion(formato_libro))
            datos_libro = tuple(cargarPublicacionDeLibro())
            unLibro = Libro(titulo = datos_publicacion[0], categoria = datos_publicacion[1], precio_base = datos_publicacion[2], nombre_autor = datos_libro[0], fecha_edicion = datos_libro[1], cantidad_paginas = datos_libro[2])
            clase_lista.agregarPublicacion(unLibro)
            system("cls")
            print(f"\t El {formato_libro} {datos_publicacion[0]} fue guardado exitosamente.")
            formato_encontrado = True
        elif formato_publicacion == '2':
            formato_audio_libro = str("Audio-Libro en CD")
            datos_publicacion = tuple(cargarDatosDePublicacion(formato_audio_libro))
            datos_audio_libro = tuple(cargarPublicacionDeAudioLibro())
            unAudioLibro = AudioLibro(titulo = datos_publicacion[0], categoria = datos_publicacion[1], precio_base = datos_publicacion[2], tiempo_reproduccion = datos_audio_libro[0], nombre_narrador = datos_audio_libro[1])
            clase_lista.agregarPublicacion(unAudioLibro)
            system("cls")
            print(f"\t El {formato_audio_libro} {datos_publicacion[0]} fue guardado exitosamente.")
            formato_encontrado = True
        else:
            print(" ERROR al ingresar el Formato de Publicación. Por favor, ingrese unas de las opciones especificadas\n")
            formato_publicacion = ingresarFormatoDePublicacion()
            formato_encontrado = False

def menu(clase_lista) -> None:
    system("cls")
    opcion = str(ingresarOpcion())
    while opcion != '0':
        system("cls")
        match opcion.lower():
            case '1':
                formato_publicacion = str(ingresarFormatoDePublicacion())
                agregarPublicacion(formato_publicacion, clase_lista)
            case '2':
                pos_lista = int(input(" Ingresar una posición de la lista: "))
                clase_lista.mostrarTipoDePublicacion(pos_lista - 1, Libro, AudioLibro)
            case '3':
                clase_lista.mostrarCantidadDePublicaciones(Libro, AudioLibro)
            case '4':
                clase_lista.mostrarPublicaciones()
            case 'mostrar':
                print("\n---PUBLICACIONES DE LA EDITORIAL COMPLETA---")
                for dato in clase_lista:
                    print("\n Datos de La Publicacion:", dato)
            case _:
                print("ERROR al ingresar la opción. Por favor ingrese una opcion especificada")
        opcion = (ingresarOpcion())
    system("cls")
    print("\n\t\t\t\t\t Fin de Programa.")