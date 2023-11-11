import speech_recognition as sr
import pyttsx3

# Configurar el reconocimiento de voz y la interacción con Google Assistant
r = sr.Recognizer()
engine = pyttsx3.init()

def e(text):
    engine.say(text)
    engine.runAndWait()

def get_user_name():
    with sr.Microphone() as source:
        e("Hola, ¿cómo te llamas?")
        audio = r.listen(source)

    try:
        user_name = r.recognize_google(audio, language='es-ES')
        return user_name
    except sr.UnknownValueError:
        e("Lo siento, no pude entender tu nombre.")
    except sr.RequestError as e:
        e("Lo siento, ha ocurrido un error al intentar reconocer tu voz. Error: {}".format(e))

def get_user_gender(user_name):
    # Obtener el primer nombre del usuario
    primer_nombre = user_name.split()[0]

    # Determinar el género del usuario en función de patrones en el nombre
    if primer_nombre.endswith(('a', 'e', 'i', 'l', 'm', 'n', 'o', 'r', 's', 't', 'u',  'y', 'z')):
        return "hombre"
    elif primer_nombre.endswith(('a', 'e', 'i', 'l', 'm', 'n', 'o', 'r', 's', 't', 'u',  'y', 'z')):
        return "mujer"
    else:
        return None
def greet_user():
    user_name = get_user_name()
    if user_name:
        user = get_user_gender(user_name)
        if user:
            if user == "hombre":
                e("Hola, señor {}. ¡Bienvenido!".format(user_name))
            elif user == "mujer":
                e("Hola, señora {}. ¡Bienvenida!".format(user_name))
            else:
                e("Lo siento, no pude identificar tu género.")
        else:
            e("Lo siento, no pude identificar tu género.")
    else:
        e("Lo siento, no pude entender tu nombre.") 
greet_user() # Saludar al usuario
