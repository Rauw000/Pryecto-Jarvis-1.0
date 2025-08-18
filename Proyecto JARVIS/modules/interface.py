#Dia 4 se realiza una interfaz para Jarvis 

import tkinter as tk
from modules.voice import listen, speak
from modules.ai_chat import chat_with_ai
from modules.memory import recall, remember
from datetime import datetime 

# Esta definicion lo que hace es escuchar a la persona y mandar una respuesta por medio de la ia 
def start_jarvis():
    user_input = listen()
    if user_input:
        response = chat_with_ai(user_input)
        chat_log.insert(tk.END, f"Tú: {user_input}\n","user")
        chat_log.insert(tk.END, f"JARVIS: {response}\n\n", "jarvis")
        chat_log.see(tk.END)
        remember("ultimo_comando", user_input)
        update_status()

def clear_chat():
    chat_log.delete(1.0 , tk.END)

def update_status():
    now = datetime.now().strftime("%H:%M:%S")
    last_command = recall("ultimo_comando") or "Ninguno"
    name = recall("nombre") or "Desconocido"
    status_label.config(text=f"Hora: {now} | Usuario: {name} | Ultimo comando {last_command}")

        
#Crear ventana 
window = tk.Tk()
window.title("JARVIS - Asistente Personal")
window.geometry("700x500")
window.configure(bg="#1e1e1e")

#Area de texto
chat_log = tk.Text(window, bg="#2e2e2e", fg="white", font=("console", 12), wrap=tk.WORD)
chat_log.tag_config("user", foreground="#00ffff")
chat_log.tag_config("jarvis", foreground="#00ff00")
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

#Panel de estado

status_label = tk.Label(window, text="", bg="#1e1e1e", fg="#cccccc", font=("Arial", 10))
status_label.pack(pady=5)
update_status()


#Boton para hablar
button_frame = tk.Frame(window, bg="#1e1e1e")
button_frame.pack(pady=10)

talk_button = tk.Button(button_frame, text="🎙️ Hablar con JARVIS", command=start_jarvis, bg="#007acc", fg="white", font=("Arial", 12))
talk_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="🧹 Limpiar pantalla", command=clear_chat, bg="#444444", fg="white", font=("Arial", 12))
clear_button.grid(row=0, column=1, padx=10)

exit_button = tk.Button(button_frame, text="❌ Salir", command=window.quit, bg="#aa0000", fg="white", font=("Arial", 12))
exit_button.grid(row=0, column=2, padx=10)


window.mainloop()

#Se creo una ventana interactiva con "tkinter"
#JARVIS ahora tiene una cara digital
# Se integro el botón para hablar y ver respuestas