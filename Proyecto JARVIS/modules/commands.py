import webbrowser
import wikipedia
from datetime import datetime
from modules.voice import speak

def handle_command(command):
    if "hora" in command:
        now = datetime.now().strftime("%H:%M") # El parentesis da referencia a la hora y los minutos
        speak(f"La hora actual es {now}")

    elif "buscar" in command:
        topic = command.replace("buscar", "").strip()
        try:
            summary = wikipedia.summary(topic, sentences=2, auto_suggest=False)
            speak(f"Esto encontré sobre {topic}: {summary}")
        except Exception:
            speak("No pude encontrar información sobre este tema.")

    elif "abrir apple music" in command:
        webbrowser.open("https://music.apple.com/")
        speak("Abriendo Apple Music.")

    elif "salir" in command:
        speak("Hasta luego.")
        exit()

    else:
        speak("No reconozco ese comando aún.")

#Dia 2 intergracion de interpretacion de comandos 
#Este modulo es para abrir aplicaciones, buscar en wikipedia 
#Decir  la hora o el clima 
#Reproducir musica
#Saludar segun la hora 