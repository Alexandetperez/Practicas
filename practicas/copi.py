import speech_recognition as sr
import pyttsx3

# Configurar el reconocimiento de voz y la interacción con Google Assistant
r = sr.Recognizer()
engine = pyttsx3.init()

def say(text):
    engine.say(text)
    engine.runAndWait()

def get_user_name():
    with sr.Microphone() as source:
        say("Hola, ¿cómo te llamas?")
        audio = r.listen(source)

    try:
        user_name = r.recognize_google(audio, language='es-ES')
        return user_name
    except sr.UnknownValueError:
        say("Lo siento, no pude entender tu nombre.")
    except sr.RequestError as e:
        say("Lo siento, ha ocurrido un error al intentar reconocer tu voz. Error: {}".format(e))

def get_user_gender(user_name):
    # Obtener el primer nombre del usuario
    primer_nombre = user_name.split()[0]

    # Determinar el género del usuario en función de patrones en el nombre
    if primer_nombre.endswith(('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')):
        return "hombre"
    elif primer_nombre.endswith(('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')):
        return "mujer"
    else:
        return None

def greet_user():
    user_name = get_user_name()
    if user_name:
        user_gender = get_user_gender(user_name)
        if user_gender:
            if user_gender == "hombre":
                say("Hola, señor {}. ¡Bienvenido!".format(user_name))
            elif user_gender == "mujer":
                say("Hola, señora {}. ¡Bienvenida!".format(user_name))
            else:
                say("Lo siento, no pude identificar tu género.")
        else:
            say("Lo siento, no pude identificar tu género.")
    else:
        say("Lo siento, no pude entender tu nombre.") 

greet_user()
