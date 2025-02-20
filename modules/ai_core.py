import random

def process_ai_command(prompt):
    respuestas = [
        "Estoy buscando información...",
        "Analizando la mejor opción...",
        "Procesando tu solicitud...",
        "Ejecutando la tarea...",
        "Organizando la información..."
    ]
    return f"🤖 {random.choice(respuestas)} Respuesta para: {prompt}"
import subprocess

OLLAMA_MODEL = "mistral"

def chat_with_ai(prompt):
    """Ejecuta Mistral en Ollama y devuelve la respuesta."""
    result = subprocess.run(["ollama", "run", OLLAMA_MODEL, prompt], capture_output=True, text=True)
    return result.stdout.strip()
