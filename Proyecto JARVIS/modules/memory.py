import json
import os

MEMORY_FILE = "assets/memory.json"

def initialize_memory():
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump({}, f)

def remember(key, value):
    initialize_memory()
    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)
    memory[key] = value
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

def recall(key):
    initialize_memory()
    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)
    return memory.get(key, None)

def forget(key):
    initialize_memory()
    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)
    if key in memory:
        del memory[key]
        with open(MEMORY_FILE, "w") as f:
            json.dump(memory, f, indent=4)