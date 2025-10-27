"""'
Programa que convierte el texto de una URL a voz mediante el uso de librerias con clases y metodos  preparadas para ello
"""

# Poner try catch pero no se cuales pueden ser los errores (honestamente pueden ser infinitos ¿o no?)

import lista_idiomas as li
from newspaper import Article
from gtts import gTTS

# url de ejemplo
# url = "https://www.hola.com/realeza/casa_espanola/20250927858276/rey-juan-carlos-campeon-del-mundo-de-vela-a-los-87-anos/"
terminado = False


while terminado == False:

    url = input("Introduzca la URL que desee: ")
    articulo = Article(url)
    articulo.download()
    articulo.parse()
    texto = articulo.text

    while True:
        idioma = input(
            "Introduzca el idioma de la locución sin acento\nRECORDAR QUE EL IDIOMA DEBE SER EL MISMO QUE EL TEXTO DE LA PAGINA ORIGINAL: "
        ).lower()

        if idioma in li.lista.keys():
            tts = gTTS(texto, lang=li.lista[idioma])
            guardado = input("¿Con qué nombre desea guardar el archivo? ")

            if not guardado.lower().endswith(".mp3"):
                guardado += ".mp3"

            tts.save(guardado)
            print("Archivo generado")
            break  # 🔹 Sale del bucle del idioma si todo salió bien
        else:
            print("Idioma no encontrado. Intente nuevamente.")

    respuesta = input("Desea realizar otra conversión (si / no) ")
    respuesta.lower()

    if respuesta == "no":
        terminado = True
