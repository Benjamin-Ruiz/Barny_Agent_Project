import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Importaciones del proyecto
from instrucciones import Instrucciones_agente
from herramientas import lista_herramientas

# 1. Carga las variables de entorno (.env)
load_dotenv()

# --- REQUERIMIENTO: DÓNDE SE CREA EL CLIENTE ---
# 2. Crea el cliente del SDK de Gemini (Utiliza GEMINI_API_KEY por defecto)
try:
    client = genai.Client()
except Exception as e:
    client = None

# Configuración del modelo y herramientas
MODEL_ID = "gemini-3.5-flash"

def inicializar_chat():
    """
    Inicializa una sesión de chat con las instrucciones y herramientas configuradas.
    """
    if client is None:
        raise ValueError("No se pudo inicializar el cliente Gemini. Verifica tu API Key.")
        
    # --- REQUERIMIENTO: DÓNDE SE ENVÍAN LAS INSTRUCCIONES y DÓNDE SE REGISTRAN LAS HERRAMIENTAS ---
    config = types.GenerateContentConfig(
        system_instruction=Instrucciones_agente,  # AQUÍ se envían las instrucciones (System Prompt)
        tools=lista_herramientas,                 # AQUÍ se registran las herramientas (Function Calling)
        temperature=0.2,
    )
    
    # Creamos el chat (mantiene el historial de la conversación)
    chat = client.chats.create(
        model=MODEL_ID,
        config=config
    )
    return chat

def enviar_mensaje(chat, mensaje_usuario: str):
    """
    Envía el mensaje del usuario al modelo y maneja la respuesta, incluyendo la ejecución
    automática de herramientas.
    """
    if not chat:
        raise ValueError("El chat no está inicializado.")
        
    # --- REQUERIMIENTO: DÓNDE SE DETECTA LA LLAMADA y DÓNDE SE EJECUTA LA FUNCIÓN ---
    # El SDK actual (genai) intercepta y detecta automáticamente si el modelo decide llamar 
    # a una herramienta. Luego ejecuta la función local de Python y le pasa el resultado de 
    # vuelta al LLM, todo encapsulado de forma transparente dentro de "send_message".
    respuesta = chat.send_message(mensaje_usuario)
    
    # --- REQUERIMIENTO: DÓNDE SE DEVUELVE EL RESULTADO ---
    # Aquí se retorna el texto final formulado por Gemini tras analizar las herramientas.
    return respuesta.text
