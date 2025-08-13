#Dia 3 Integracion de IA conversacional OpenAI

import openai
from modules.voice import speak

openai.api_key = "API_KEY"  # Reemplaza con tu clave real

def chat_with_ai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente llamado JARVIS que ayuda a Raúl."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = response.choices[0].message.content
        speak(reply)
        return reply
    except Exception as e:
        speak("Hubo un error al conectar con la inteligencia artificial.")
        print(e)
        return ""