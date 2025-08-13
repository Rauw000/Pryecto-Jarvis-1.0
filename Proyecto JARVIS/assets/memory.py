#Estructura de memoria basica

import json
import os

MEMORY_FILE = "assets/memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    return {}

def save_memory(data):
    with open(MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=4)

def remember(key, value):
    memory = load_memory()
    memory[key] = value
    save_memory(memory)

def recall(key):
    memory = load_memory()
    return memory.get(key, None)

#- Se integró OpenAI para conversación natural
#- JARVIS ahora responde preguntas complejas
#- Se creó un sistema de memoria básica con JSON
#- Próximo paso: interfaz visual y comandos avanzados