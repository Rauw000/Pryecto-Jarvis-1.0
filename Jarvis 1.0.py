#Inicio programa Jarvis 1.0
 
#Día 1 - Preparación 

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
        command = recognizer.recognize_google(audio, language="es-ES")#traduce el audio a texto 
        print(f"Dijiste: {command}")
        return command.lower()# Counvierte el texto a minusculas para facilitar el analisis
    #Manejo de errores
    except sr.UnknownValueError:# Si no se puede entender el audio
        speak("No entedi lo que dijiste.")
        return ""
    except sr.RequestError:# Si hay un problema con el servicio de Google
        speak("Hubo un problema con el sercio de reconocimiento de voz.")
        return ""
    
#Dia 2 intergracion de interpretacion de comandos 
#Este modulo es para abrir aplicaciones, buscar en wikipedia 
#Decir  la hora o el clima 
#Reproducir musica
#Saludar segun la hora 

import webbrowser
import wikipedia
from datetime import datetime
from modules.voice import speak

def handel_command(command):
        """Interpreta y ejecuta comandos basicos"""

        if "hora" in command:
            now = datetime.now().strftime("%H:%M")# El parentesis da referencia a la hora y los minutos
            speak(f"La hora actual es {now}")

        elif "buscar" in command:
            topic = command.replace("buscar", "").strip()
            try:
                summary =wikipedia.summary(topic, sentences=2, auto_suggest=False)
                speak(f"Esto encontré sobre {topic}: {summary}")
            except Exception:
                speak("No pude encontrar informacion sobre este tema.")

        elif "abrir apple music" in command:
            webbrowser.open("https://music.apple.com/") 
            speak("Abriendo Apple Music.")
        elif "salir" in command:
            speak("Hasta luego.")
            exit()
        else:
            speak("No reconozco ese comando aún.")

#Dia 3 Integracion de IA conversacional OpenAI





    