#Inicio programa Jarvis 1.0
 
##Día 1 - Preparación 

## Estructura de escuchar voz y conventirla en texto
## Usar texto para generar una respuesta hablada 

import speech_recognition as sr
import pyttsx3

# Inicializar el motor de texto a voz
engine = pyttsx3.init() 
engine.setProperty('rate', 150)  # Ajustar la velocidad de habla

engine.setProperty('volumen',1.0) # Ajustar el volumen (0.0 a 1.0)
def speak(text):
    """Escucha el microfono y devuelve texto"""
    #Esta funcion hace que Jarvis hable
    recognizer = sr.Recognizer()
    engine.say(text) # le dice al motor de texto a voz que hable
    engine.runAndWait()  # Espera a que termine de hablar
   
   #Esta funcion hace que Jarvis escuche
def listen():
    """Escucha el microfono y devuelve texto"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
    recognizer.adjust_for_ambient_noise(source)# Ajusta el reconocimiento para ignorar el ruido de fondo
    audio = recognizer.listen(source)# listen source graba el audio del micrófono
    #Procesar el audio y convertirlo a texto
    try:
        commmand = recognizer.recognize_google(audio, language="es-Es")# Envia el audio a google y recive texto
        print(f"Dijiste: {command}")
        return command.lower()# Counvierte el texto a minusculas para facilitar el analisis
    #Manejo de errores
    except sr.UnknownValueError:# Si no se puede entender el audio
        speak("No entedi lo que dijiste.")
        return ""
    except sr.RequestError:# Si hay un problema con el servicio de Google
        speak("Hubo un problema con el sercio de reconocimiento de voz.")
        return ""
    

    