import sys
from google.genai import errors
from agente import inicializar_chat, enviar_mensaje

def imprimir_banner():
    print("=" * 60)
    print(" " * 20 + "BARNY AGENT")
    print(" " * 5 + "Asistente de Arquitectura y Calidad de Software")
    print("=" * 60)
    print("Escribe 'salir' o 'exit' para terminar.\n")

def main():
    imprimir_banner()

    # Manejo de error de inicialización (API Key, Conexión)
    try:
        chat = inicializar_chat()
    except ValueError as e:
        print(f"❌ Error de configuración: {e}")
        print("Asegúrate de tener un archivo .env con tu GEMINI_API_KEY.")
        sys.exit(1)
    except errors.APIError as e:
        print(f"❌ Error de API al conectar: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        sys.exit(1)

    print("🤖 Barny está listo. ¿En qué puedo ayudarte hoy?\n")

    while True:
        try:
            mensaje = input("Tú > ")
            
            if mensaje.lower() in ['salir', 'exit', 'quit']:
                print("¡Hasta luego! Recuerda seguir los principios SOLID.")
                break
                
            if not mensaje.strip():
                print("⚠️ Mensaje vacío. Por favor escribe algo.")
                continue

            print("Barny está analizando...")
            
            # Enviar el mensaje y manejar la respuesta
            respuesta = enviar_mensaje(chat, mensaje)
            
            if not respuesta:
                print("⚠️ El modelo no devolvió una respuesta válida (Respuesta vacía).")
            else:
                print("\n🤖 Barny:\n")
                print(respuesta)
                print("-" * 60)

        # Errores específicos del SDK
        except errors.APIError as e:
            if "quota" in str(e).lower() or 429 in e.code:
                print("❌ Error: Cuota de API agotada. Intenta más tarde.")
            else:
                print(f"❌ Error de la API de Gemini: {e}")
        
        # Cualquier otro error (herramientas fallando, conexión perdida)
        except Exception as e:
            print(f"❌ Error inesperado: Ocurrió un problema procesando tu solicitud.")
            print(f"Detalle: {e}")
            
        except KeyboardInterrupt:
            print("\nOperación cancelada por el usuario. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
