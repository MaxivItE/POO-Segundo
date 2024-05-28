from ClaseLibro import Libro
from ClaseAudioLibro import AudioLibro

def test(clase_lista) -> None:
    libro1 = Libro("CAPITALISMO, SOCIALISMO Y LA TRAMPA NEOCLASICA", "Teoría y filosofía económicas", 26900, "Javier Milei", "26/04/2024", 376)
    libro2 = Libro("LA FELICIDAD", "Meditación, entre otros", 27900, "Gabriel Rolon", "30/11/2023", 392)
    libro3 = Libro("Genética molecular humana", "Ciencias de la vida y Biología", 183828.50, "Strachan, Tom, Read, Andrew P.", "19/03/1999", 672)
    audio_libro1 = AudioLibro("Cuéntame esta noche", "Novela romántica", 19900, 450, "Eva Coll")
    audio_libro2 = AudioLibro("Libre del miedo", "Autoayuda", 15900, 533, "Rosa María Cifuentes Castañeda")
    audio_libro3 = AudioLibro("Cómo llamarte amor 1. A gritos", "Ficción", 12500, 1120, "Alba Iago")
    clase_lista.agregarPublicacion(audio_libro3)
    clase_lista.agregarPublicacion(libro3)
    clase_lista.agregarPublicacion(audio_libro2)
    clase_lista.agregarPublicacion(libro1)
    clase_lista.agregarPublicacion(audio_libro1)
    clase_lista.agregarPublicacion(libro2)