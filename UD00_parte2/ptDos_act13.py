import requests

#Pedimos al usuario que introduzca una especie de personaje de Rick y Morty.
especie = input(
    "Introduce una especie: "
)

#Url de la API de Rick y Morty para consultar personajes.
url = "https://rickandmortyapi.com/api/character/"


# Indicamos a la API que queremos buscar
# personajes de la especie introducida.
parametros = {
    "species": especie
}


#Realizamos la petición a la API
respuesta = requests.get(
    url,
    params=parametros
)

#Comprobamos si la respuesta ha sido correcta (código 200)
if respuesta.status_code != 200:

    print("Error al consultar la API.")

else:

    # Convertimos la respuesta JSON
    # en datos de Python.
    datos = respuesta.json()


    #Mostramos los personajes encontrados

    # Comprobamos si existen resultados.
    if "results" not in datos:

        print(
            "No se han encontrado personajes."
        )

    else:

        personajes = datos["results"]

        print(
            "\nPersonajes de la especie:",
            especie
        )

        print("------------------------------")

        for personaje in personajes:

            print(
                personaje["name"]
            )