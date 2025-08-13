#Inicio programa Jarvis 1.0
 
#Día 1 - Preparación 

## Estructura de escuchar voz y conventirla en texto
## Usar texto para generar una respuesta hablada 

# main.py
from modules.voice import listen, speak
from modules.commands import handle_command
from modules.ai_chat import chat_with_ai
from modules.memory import remember

def JARVIS():
    speak("Hola Raúl, soy JARVIS. ¿En qué puedo ayudarte hoy?")
    while True:
        command = listen()
        if not command:
            continue
        remember("Ultimo comando", command)

        if "jarvis" in command.lower():
            chat_with_ai(command)
        else:
            handle_command(command)

if __name__ == "__main__":
    JARVIS()
    



