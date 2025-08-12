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

import openai
from modules.voice import speak

openai.api_key = "API_KEY" #Remplazar por la clave real

def chat_whit_ai(prompt):
    """Envia el texto a OpenAI y devuelve la respuesta"""
    try:
        response =openai.ChatCompletion.create(
            model="gpt-3,5-turbo",

            messages=[
                {"role":"systen","content":"Eres un asistente llamado JARVIS que ayuda a Raul."}, # aca puedes cambiar para que diga a la persona que esta ayudando
                {"role":"user","content":prompt}
            ]
        )
        reply = response.choices[0].message.content
        speak(reply)
        return reply
    except Exception as e:
        speak("Hubo un error al conectar con la inteligencia artificial.")
        print(e)
        return ""
    
#Estructura de memoria basica
import json
import os

MEMORY_FILE = "assets/memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE,"r") as file:
            return json.load(file)
        return{}
    
def save_memory(data):
    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=4)

def remember(key, value):
    memory = load_memory()
    memory[key] = value
    save_memory(memory)

def recall(key):
    memmory = load_memory()
    return memory.get(key, None)

#- Se integró OpenAI para conversación natural
#- JARVIS ahora responde preguntas complejas
#- Se creó un sistema de memoria básica con JSON
#- Próximo paso: interfaz visual y comandos avanzados

    



#Dia 4 se realiza una interfaz para Jarvis 
import tkinter as tk
from modules.voice import listen, speak 
from modules.ai.chat import chat_whit_ai


# Esta definicion lo que hace es escuchar a la persona y mandar una respuesta por medio de la ia 
def start_jarvis():
    user_input = listen()
    if user_input:
        response = chat_whit_ai(user_input)
        chat_log.insert(tk.END, f"Tu: {user_input}\n")
        chat_log.insert(tk.END, f"JARVIS: {response}\n\n")

#Crear ventana 
window = tk.TK()
window.title("JARVIS - Asistente Personal")
window.geometry("600x400")
window.configure(bg="#1e1e1e")

#Area de texto
chat_log = tk.Text(window, bg="#2e2e2e", fg="white", font=("console",12))
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

#Boton para hablar 
talk_button = tk.Button(window, text="Hablar con JARVIS", command=start_jarvis, bg="#007acc", fg="white", font=("Arial", 12))
talk_button.pack(pady=10)

window.mainloop()

#Se creo una ventana interactiva con "tkinter"
#JARVIS ahora tiene una cara digital
# Se integro el botón para hablar y ver respuestas







