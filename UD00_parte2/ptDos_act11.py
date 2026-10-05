import hashlib

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

#Función para calcular el hash SHA-1 de un texto
def calcular_sha1(texto):
    """
    Recibe un texto y devuelve su hash SHA-1.

    Ejemplo:
        calcular_sha1("1234")
    """

    # Convertimos el texto a bytes.
    texto_bytes = texto.encode("utf-8")

    # Calculamos el hash SHA-1.
    hash_sha1 = hashlib.sha1(texto_bytes)

    # Convertimos el resultado a hexadecimal.
    return hash_sha1.hexdigest()

#ler usuarios desde users.csv

def cargar_usuarios():
    """
    Lee users.csv y devuelve un diccionario.

    Formato del archivo:

        usuario:hash_sha1
    """

    usuarios = {}

    try:

        with open(
            "users.csv",
            "r",
            encoding="utf-8"
        ) as archivo:

            for linea in archivo:

                linea = linea.strip()

                # Ignoramos líneas vacías.
                if linea == "":
                    continue

                # Separamos usuario y contraseña.
                partes = linea.split(":", 1)

                # Comprobamos que haya dos partes.
                if len(partes) != 2:
                    continue

                usuario = partes[0]
                password_hash = partes[1]

                usuarios[usuario] = password_hash

    except FileNotFoundError:

        print("ERROR: No se encuentra users.csv")

    return usuarios

    #Interfaz
class LoginLayout(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        # Colocamos los elementos verticalmente.
        self.orientation = "vertical"

        # Espacio entre elementos.
        self.spacing = 10

        # Márgenes internos.
        self.padding = 20


        #Texto para el usuario
        self.add_widget(
            Label(
                text="Usuario"
            )
        )

        #Usuarios
        self.usuario_input = TextInput(
            multiline=False
        )

        self.add_widget(
            self.usuario_input
        )

        #Texto para la contraseña
        self.add_widget(
            Label(
                text="Contraseña"
            )
        )

        #Componente para introducir la contraseña
        self.password_input = TextInput(
            multiline=False,
            password=True
        )

        self.add_widget(
            self.password_input
        )

        #Botón para comprobar el login
        boton = Button(
            text="comprobar"
        )

        # Cuando pulsamos el botón,
        # ejecutamos comprobar_login().
        boton.bind(
            on_press=self.comprobar_login
        )

        self.add_widget(
            boton
        )

        #Resultado del login (OK o ERROR)
        self.resultado = Label(
            text=""
        )

        self.add_widget(
            self.resultado
        )

    
    #Comprobamos el login cuando pulsamos el botón

    def comprobar_login(self, instancia):

        # Cargamos los usuarios.
        usuarios = cargar_usuarios()

        # Obtenemos el usuario escrito.
        usuario = self.usuario_input.text

        # Obtenemos la contraseña escrita.
        password = self.password_input.text

        # Comprobamos si el usuario existe
        if usuario not in usuarios:

            self.resultado.text = "ERROR"

            return

        #Calculamos el hash SHA-1 de la contraseña escrita
        password_hash = calcular_sha1(
            password
        )

        #Comprobamos si el hash coincide con el del usuario
        if password_hash == usuarios[usuario]:

            self.resultado.text = "OK"

        else:

            self.resultado.text = "ERROR"


#Aplicación Kivy
class LoginApp(App):

    def build(self):

        return LoginLayout()


#iniciar la aplicación
if __name__ == "__main__":

    LoginApp().run()