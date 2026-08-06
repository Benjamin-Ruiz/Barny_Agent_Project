import json

def analizar_requisitos(texto_del_caso: str) -> str:
    """
    Analiza un caso de estudio o requerimiento y devuelve una lista estructurada de entidades.
    """
    # 1. Validación de entrada
    if not texto_del_caso or not isinstance(texto_del_caso, str) or len(texto_del_caso.strip()) == 0:
        return json.dumps({"error": "Validación fallida: El texto del caso no puede estar vacío."})
    
    # 2. Manejo básico de errores
    try:
        resultado = {
            "estado": "análisis completado",
            "mensaje": "Instrucción para el agente: Estructura tu análisis basándote en este formato.",
            "estructura_esperada": {
                "requisitos_funcionales": [],
                "actores_involucrados": [],
                "datos_principales": [],
                "restricciones_del_sistema": [],
                "ambiguedades_detectadas": []
            }
        }
        return json.dumps(resultado)
    except Exception as e:
        return json.dumps({"error": f"Error inesperado al analizar requisitos: {str(e)}"})


def revisar_codigo(codigo: str) -> str:
    """
    Revisa un fragmento de código y devuelve hallazgos estructurales y de calidad.
    """
    if not codigo or not str(codigo).strip():
        return json.dumps({"error": "Validación fallida: El código proporcionado está incompleto o vacío."})
        
    try:
        resultado = {
            "estado": "revisión completada",
            "mensaje": "Instrucción para el agente: Analiza el código proporcionado usando las siguientes categorías.",
            "categorias_a_evaluar": [
                "legibilidad",
                "claridad_de_nombres",
                "funciones_extensas",
                "codigo_duplicado_DRY",
                "responsabilidades_KISS",
                "manejo_de_errores"
            ]
        }
        return json.dumps(resultado)
    except Exception as e:
        return json.dumps({"error": f"Error interno al revisar código: {str(e)}"})


def generar_pruebas(funcionalidad: str) -> str:
    """
    Genera casos de prueba estructurados para una funcionalidad específica.
    """
    if not funcionalidad or not str(funcionalidad).strip():
        return json.dumps({"error": "Validación fallida: El requerimiento a probar es ambiguo o vacío."})
        
    try:
        resultado = {
            "estado": "estructura de pruebas lista",
            "formato_sugerido": "Given-When-Then",
            "casos_requeridos": {
                "caso_correcto": "Escenario ideal o 'Happy Path'",
                "caso_incorrecto": "Datos inválidos o errores de usuario",
                "caso_limite": "Valores extremos, nulos, vacíos o máximos",
                "resultado_esperado": "Lo que la función debe retornar o el efecto secundario esperado"
            }
        }
        return json.dumps(resultado)
    except Exception as e:
        return json.dumps({"error": f"Error interno al generar pruebas: {str(e)}"})


def evaluar_solid(codigo: str) -> str:
    """
    Evalúa estrictamente un fragmento de código contra los 5 principios SOLID.
    """
    if not codigo or len(str(codigo).strip()) < 5:
        return json.dumps({"error": "Validación fallida: El fragmento de código es muy corto para evaluar SOLID."})
        
    try:
        resultado = {
            "estado": "evaluación SOLID iniciada",
            "criterios": {
                "SRP": "Single Responsibility Principle",
                "OCP": "Open/Closed Principle",
                "LSP": "Liskov Substitution Principle",
                "ISP": "Interface Segregation Principle",
                "DIP": "Dependency Inversion Principle"
            }
        }
        return json.dumps(resultado)
    except Exception as e:
        return json.dumps({"error": f"Error interno al evaluar SOLID: {str(e)}"})


def validar_nombres(codigo: str) -> str:
    """
    Revisa y valida que los nombres de variables, funciones y clases cumplan con Clean Code.
    """
    if not codigo or not str(codigo).strip():
        return json.dumps({"error": "Validación fallida: No hay código para validar nombres."})
        
    try:
        resultado = {
            "estado": "validación de nombres",
            "reglas_a_aplicar": [
                "Nombres descriptivos e intencionales",
                "Evitar números mágicos",
                "Evitar abreviaturas incomprensibles",
                "Consistencia en el estilo (camelCase, snake_case)"
            ]
        }
        return json.dumps(resultado)
    except Exception as e:
        return json.dumps({"error": f"Error al validar nombres: {str(e)}"})


def analisis_seguridad_basico(codigo: str) -> str:
    """
    Busca vulnerabilidades comunes en el código (ej. inyección SQL, secretos en duro).
    """
    if not codigo or not str(codigo).strip():
        return json.dumps({"error": "Validación fallida: No hay código a auditar."})
        
    try:
        resultado = {
            "estado": "auditoría de seguridad",
            "puntos_de_control_OWASP": [
                "Inyección de dependencias / SQL / XSS",
                "Secretos o contraseñas hardcodeadas",
                "Validación insuficiente de entradas de usuario",
                "Manejo inseguro de datos sensibles"
            ]
        }
        return json.dumps(resultado)
    except Exception as e:
        return json.dumps({"error": f"Error interno en análisis de seguridad: {str(e)}"})


def generar_checklist_calidad(modulo: str) -> str:
    """
    Genera una lista de verificación antes de dar por terminado un módulo de software.
    """
    if not modulo or not str(modulo).strip():
        return json.dumps({"error": "Validación fallida: Debe especificar el nombre del módulo."})
        
    try:
        resultado = {
            "estado": "checklist generada",
            "items": [
                "El código cumple con los requisitos iniciales.",
                "No hay código comentado ni 'TODOs' olvidados.",
                "Todas las variables y funciones tienen nombres descriptivos.",
                "Los casos límite están manejados.",
                "Se incluye manejo de excepciones (try/except)."
            ]
        }
        return json.dumps(resultado)
    except Exception as e:
        return json.dumps({"error": f"Error al generar checklist: {str(e)}"})


def detectar_code_smells(codigo: str) -> str:
    """
    Analiza el código en busca de 'code smells' o malos olores de programación.
    """
    if not codigo or not str(codigo).strip():
        return json.dumps({"error": "Validación fallida: No se proporcionó código."})
        
    try:
        resultado = {
            "estado": "análisis de code smells",
            "smells_a_buscar": [
                "Funciones con más de 3-4 parámetros",
                "Funciones demasiado largas (>20 líneas)",
                "Lógica anidada profunda (Arrow Anti-Pattern)",
                "Clases Dios (God Classes) que hacen demasiado"
            ]
        }
        return json.dumps(resultado)
    except Exception as e:
        return json.dumps({"error": f"Error interno al buscar smells: {str(e)}"})


def planificar_tareas(requisitos_completos: str) -> str:
    """
    Desglosa un problema complejo en pequeñas tareas o historias de usuario accionables.
    """
    if not requisitos_completos or not str(requisitos_completos).strip():
        return json.dumps({"error": "Validación fallida: Faltan los requisitos completos."})
        
    try:
        resultado = {
            "estado": "plan de tareas creado",
            "instruccion": "Divide el problema en tareas pequeñas que se puedan programar independientemente, priorizando dependencias base primero."
        }
        return json.dumps(resultado)
    except Exception as e:
        return json.dumps({"error": f"Error interno al planificar tareas: {str(e)}"})


def verificar_manejo_errores(codigo: str) -> str:
    """
    Revisa si un código está preparado para fallar de manera controlada.
    """
    if not codigo or not str(codigo).strip():
        return json.dumps({"error": "Validación fallida: El código está vacío."})
        
    try:
        resultado = {
            "estado": "revisión de excepciones",
            "validaciones_requeridas": [
                "Bloques try/catch o try/except implementados donde hay riesgo de fallo.",
                "Mensajes de error informativos pero no exponen información del sistema.",
                "El sistema no colapsa silenciosamente (fail-fast)."
            ]
        }
        return json.dumps(resultado)
    except Exception as e:
        return json.dumps({"error": f"Error interno en la verificación de errores: {str(e)}"})

# Lista de todas las herramientas disponibles para exportar a agente.py
lista_herramientas = [
    analizar_requisitos,
    revisar_codigo,
    generar_pruebas,
    evaluar_solid,
    validar_nombres,
    analisis_seguridad_basico,
    generar_checklist_calidad,
    detectar_code_smells,
    planificar_tareas,
    verificar_manejo_errores
]
