import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Importaciones del proyecto
from instrucciones import Instrucciones_agente
from herramientas import lista_herramientas

# 1. Carga las variables de entorno (.env)
load_dotenv()

# 2. Crea el cliente del SDK de Gemini
# Utiliza la variable GEMINI_API_KEY por defecto
try:
    client = genai.Client()
except Exception as e:
    client = None

# Configuración del modelo y herramientas
# Usamos un modelo que soporte llamadas a herramientas (gemini-2.5-flash)
MODEL_ID = "gemini-2.5-flash"

def inicializar_chat():
    """
    Inicializa una sesión de chat con las instrucciones y herramientas configuradas.
    """
    if client is None:
        raise ValueError("No se pudo inicializar el cliente Gemini. Verifica tu API Key.")
        
    config = types.GenerateContentConfig(
        system_instruction=Instrucciones_agente,
        tools=lista_herramientas,
        temperature=0.2, # Baja temperatura para código más preciso y menos alucinaciones
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
    automática de herramientas (Function Calling) soportada por el SDK.
    """
    if not chat:
        raise ValueError("El chat no está inicializado.")
        
    # El SDK actual maneja automáticamente la invocación de funciones de Python
    # si se proveen en la configuración.
    respuesta = chat.send_message(mensaje_usuario)
    return respuesta.text
