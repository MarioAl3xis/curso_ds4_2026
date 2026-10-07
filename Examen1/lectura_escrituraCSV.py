
"""
GARCÍA RODRÍGUEZ MARIO ALEXIS, DS4 5:00-6:00
que usaste?: Usé como apoyo una herramienta de IA que me ayudó un poco cuando me atoré en el código.
que modelo: Chat GPT, no es programadora pero si me sirve bastante.
#ue version: GPT-5.6 Luna

"""
import csv
import argparse
import re
from collections import Counter

class Frase:

    def __init__(self, frase, pelicula):
        self.frase = frase
        self.pelicula = pelicula

    def __str__(self):
        return f'"{self.frase}" - {self.pelicula}'




def leer_csv(nombre_archivo):

    frases = []

    with open(nombre_archivo, "r", encoding="utf-8-sig", newline="") as archivo:

        lector = csv.DictReader(archivo)

        for fila in lector:

            frase = Frase(
                fila["Frase"],
                fila["Película"]
            )

            frases.append(frase)

    return frases





def escribir_csv(nombre_archivo, frases):

    with open(nombre_archivo, "w", encoding="utf-8", newline="") as archivo:

        escritor = csv.writer(archivo)

        # Encabezados
        escritor.writerow(["Frase", "Película"])

        # Frases
        for frase in frases:
            escritor.writerow([
                frase.frase,
                frase.pelicula
            ])



def buscar_palabra(frases):

    palabra = input("\nEscribe la palabra que deseas buscar: ").strip()

    if palabra == "":
        print("\nNo escribiste ninguna palabra.")
        return

    encontrados = []

    # Buscar la palabra completa, sin importar mayúsculas/minúsculas
    patron = re.compile(
        r"(?<!\w)" + re.escape(palabra) + r"(?!\w)",
        re.IGNORECASE
    )

    for frase in frases:

        if patron.search(frase.frase):
            encontrados.append(frase)

    print("\n========================================")
    print("RESULTADOS DE LA BÚSQUEDA")
    print("========================================")

    if len(encontrados) == 0:

        print(f'\nNo se encontró la palabra "{palabra}".')

    else:

        print(f'\nSe encontraron {len(encontrados)} frase(s):\n')

        for frase in encontrados:
            print(frase)

    print()



def agregar_frase(frases, nombre_archivo):

    print("\n========================================")
    print("AGREGAR NUEVA FRASE")
    print("========================================")

    texto = input("\nEscribe la frase: ").strip()

    if texto == "":
        print("\nLa frase no puede estar vacía.")
        return

    pelicula = input("Escribe la película: ").strip()

    if pelicula == "":
        print("\nLa película no puede estar vacía.")
        return

    nueva_frase = Frase(texto, pelicula)

    frases.append(nueva_frase)

    # Guardar inmediatamente en el archivo
    escribir_csv(nombre_archivo, frases)

    print("\n¡Frase agregada correctamente!")
    print(nueva_frase)




def contar_palabras_diferentes(frases):

    palabras = set()

    for frase in frases:

        # Extraemos solamente palabras
        palabras_frase = re.findall(
            r"[a-záéíóúüñA-ZÁÉÍÓÚÜÑ0-9]+",
            frase.frase.lower()
        )

        for palabra in palabras_frase:
            palabras.add(palabra)

    return len(palabras)



def mostrar_estadisticas(frases):

    palabras_diferentes = contar_palabras_diferentes(frases)

    numero_frases = len(frases)

    peliculas = set()

    for frase in frases:
        peliculas.add(frase.pelicula)

    numero_peliculas = len(peliculas)

    print("\n========================================")
    print("ESTADÍSTICAS")
    print("========================================")

    print(f"\nPalabras diferentes: {palabras_diferentes}")
    print(f"Número de frases:    {numero_frases}")
    print(f"Número de películas: {numero_peliculas}")

    print()



def mostrar_frases_por_pelicula(frases):

    peliculas = {}

    # Agrupar las frases por película
    for frase in frases:

        if frase.pelicula not in peliculas:
            peliculas[frase.pelicula] = []

        peliculas[frase.pelicula].append(frase)

    # Ordenar de mayor a menor cantidad de frases
    peliculas_ordenadas = sorted(
        peliculas.items(),
        key=lambda elemento: len(elemento[1]),
        reverse=True
    )

    print("\n========================================")
    print("FRASES POR PELÍCULA")
    print("========================================")

    for pelicula, lista_frases in peliculas_ordenadas:

        print("\n----------------------------------------")
        print(f"{pelicula} ({len(lista_frases)} frase(s))")
        print("----------------------------------------")

        for frase in lista_frases:
            print(f'"{frase.frase}"')

    print()


def mostrar_menu():

    print("\n")
    print("========================================")
    print("       FRASES CÉLEBRES DE PELÍCULAS")
    print("========================================")
    print()
    print("1. Buscar una palabra")
    print("2. Agregar una nueva frase")
    print("3. Mostrar estadísticas")
    print("4. Mostrar frases por película")
    print("5. Salir")
    print()
    print("========================================")



def main():

   

    parser = argparse.ArgumentParser(
        description="Programa para administrar frases célebres de películas."
    )

    parser.add_argument(
        "-i",
        "--input",
        required=True,
        help="Archivo CSV de entrada"
    )

    parser.add_argument(
        "-o",
        "--output",
        required=True,
        help="Archivo CSV de salida"
    )

    args = parser.parse_args()


    try:

        frases = leer_csv(args.input)

    except FileNotFoundError:

        print("\nERROR: No se encontró el archivo de entrada.")
        print(f"Archivo: {args.input}")
        return

    except KeyError as error:

        print("\nERROR: El archivo CSV no tiene las columnas esperadas.")
        print("Se esperan las columnas:")
        print("Frase")
        print("Película")
        print(f"\nColumna problemática: {error}")
        return

 

    escribir_csv(args.output, frases)

    print("\n========================================")
    print("ARCHIVO CARGADO CORRECTAMENTE")
    print("========================================")
    print(f"Frases cargadas: {len(frases)}")
    print(f"Archivo de salida: {args.output}")


    while True:

        mostrar_menu()

        opcion = input("Selecciona una opción: ").strip()

        # ----------------------------------------------------
        # OPCIÓN 1
        # ----------------------------------------------------

        if opcion == "1":

            buscar_palabra(frases)

        # ----------------------------------------------------
        # OPCIÓN 2
        # ----------------------------------------------------

        elif opcion == "2":

            agregar_frase(frases, args.output)

        # ----------------------------------------------------
        # OPCIÓN 3
        # ----------------------------------------------------

        elif opcion == "3":

            mostrar_estadisticas(frases)

        # ----------------------------------------------------
        # OPCIÓN 4
        # ----------------------------------------------------

        elif opcion == "4":

            mostrar_frases_por_pelicula(frases)

        # ----------------------------------------------------
        # OPCIÓN 5
        # ----------------------------------------------------

        elif opcion == "5":

            # Guardar antes de salir
            escribir_csv(args.output, frases)

            print("\nLos cambios fueron guardados.")
            print("Programa terminado.")

            break



        else:

            print("\nOpción no válida. Intenta nuevamente.")




if __name__ == "__main__":
    main()