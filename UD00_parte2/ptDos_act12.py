# Pillow permite abrir y trabajar con imágenes.
from PIL import Image

# pytesseract permite utilizar Tesseract desde Python.
import pytesseract


#Abrimos la imagen que queremos analizar
imagen = Image.open("imagen.png")


#Reconocemos el texto de la imagen

# image_to_string analiza la imagen y devuelve
# el texto que ha conseguido reconocer.
# lang="spa" indica que el texto está en español.
texto = pytesseract.image_to_string(
    imagen,
    lang="spa"
)

#Mostramos el resultado por pantalla
print("Texto reconocido:")
print("------------------")
print(texto)