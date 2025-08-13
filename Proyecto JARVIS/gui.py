#Dia 4 se realiza una interfaz para Jarvis 

import tkinter as tk
from modules.voice import listen, speak
from modules.ai_chat import chat_with_ai

# Esta definicion lo que hace es escuchar a la persona y mandar una respuesta por medio de la ia 
def start_jarvis():
    user_input = listen()
    if user_input:
        response = chat_with_ai(user_input)
        chat_log.insert(tk.END, f"Tú: {user_input}\n")
        chat_log.insert(tk.END, f"JARVIS: {response}\n\n")
        
#Crear ventana 
window = tk.Tk()
window.title("JARVIS - Asistente Personal")
window.geometry("600x400")
window.configure(bg="#1e1e1e")

#Area de texto
chat_log = tk.Text(window, bg="#2e2e2e", fg="white", font=("console", 12))
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

#Boton para hablar
talk_button = tk.Button(window, text="Hablar con JARVIS", command=start_jarvis, bg="#007acc", fg="white", font=("Arial", 12))
talk_button.pack(pady=10)

window.mainloop()

#Se creo una ventana interactiva con "tkinter"
#JARVIS ahora tiene una cara digital
# Se integro el botón para hablar y ver respuestas