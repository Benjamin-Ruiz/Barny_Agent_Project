import json

def analizar_requisitos(texto_del_caso: str) -> str:
    """
    Analiza un caso de estudio o requerimiento y devuelve una lista estructurada de entidades.
    Útil en la fase de Gather Context & Analyze Requirements.
    
    Args:
        texto_del_caso: El texto completo del requerimiento o caso de estudio a analizar.
    
    Returns:
        Un string en formato JSON con los requisitos, actores, datos, restricciones y ambigüedades.
    """
    # En un entorno real, aquí se podría aplicar lógica local compleja. 
    # Para el propósito de Function Calling, devolvemos un esquema estructurado que el agente usará.
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


def revisar_codigo(codigo: str) -> str:
    """
    Revisa un fragmento de código y devuelve hallazgos estructurales y de calidad.
    Útil en la fase de Self Correction o al revisar código proporcionado por el usuario.
    
    Args:
        codigo: El fragmento de código fuente a revisar.
        
    Returns:
        Un string en formato JSON con los hallazgos de revisión.
    """
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


def generar_pruebas(funcionalidad: str) -> str:
    """
    Genera casos de prueba estructurados para una funcionalidad específica.
    Útil en la fase de Verify.
    
    Args:
        funcionalidad: Descripción de la funcionalidad o código a probar.
        
    Returns:
        Un string en formato JSON con la estructura de los casos de prueba a proponer.
    """
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


def evaluar_solid(codigo: str) -> str:
    """
    Evalúa estrictamente un fragmento de código contra los 5 principios SOLID.
    Útil para asegurar la escalabilidad de la arquitectura.
    
    Args:
        codigo: El código orientado a objetos a analizar.
        
    Returns:
        Un string en formato JSON para organizar el reporte de SOLID.
    """
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


def validar_nombres(codigo: str) -> str:
    """
    Revisa y valida que los nombres de variables, funciones y clases cumplan con Clean Code.
    Útil para mejorar la legibilidad del proyecto.
    
    Args:
        codigo: El fragmento de código a analizar.
        
    Returns:
        JSON con directrices de nombres.
    """
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


def analisis_seguridad_basico(codigo: str) -> str:
    """
    Busca vulnerabilidades comunes en el código (ej. inyección SQL, secretos en duro).
    Útil en la fase de revisión antes de considerar el código como finalizado.
    
    Args:
        codigo: Fragmento de código a auditar.
        
    Returns:
        JSON con el reporte de seguridad esperado.
    """
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


def generar_checklist_calidad(modulo: str) -> str:
    """
    Genera una lista de verificación antes de dar por terminado un módulo de software.
    Útil en la fase Final Response.
    
    Args:
        modulo: Nombre o descripción del módulo finalizado.
        
    Returns:
        JSON con la checklist de calidad.
    """
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


def detectar_code_smells(codigo: str) -> str:
    """
    Analiza el código en busca de 'code smells' o malos olores de programación.
    Útil para la refactorización (Self Correction).
    
    Args:
        codigo: El código a analizar.
        
    Returns:
        JSON con los hallazgos.
    """
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


def planificar_tareas(requisitos_completos: str) -> str:
    """
    Desglosa un problema complejo en pequeñas tareas o historias de usuario accionables.
    Útil en la fase Plan Solution.
    
    Args:
        requisitos_completos: Requerimientos del sistema a desarrollar.
        
    Returns:
        JSON estructurado con las tareas.
    """
    resultado = {
        "estado": "plan de tareas creado",
        "instruccion": "Divide el problema en tareas pequeñas que se puedan programar independientemente, priorizando dependencias base primero."
    }
    return json.dumps(resultado)


def verificar_manejo_errores(codigo: str) -> str:
    """
    Revisa si un código está preparado para fallar de manera controlada.
    Útil para asegurar la resiliencia del software.
    
    Args:
        codigo: El código a auditar.
        
    Returns:
        JSON con directrices de resiliencia.
    """
    resultado = {
        "estado": "revisión de excepciones",
        "validaciones_requeridas": [
            "Bloques try/catch o try/except implementados donde hay riesgo de fallo.",
            "Mensajes de error informativos pero no exponen información del sistema.",
            "El sistema no colapsa silenciosamente (fail-fast)."
        ]
    }
    return json.dumps(resultado)

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
