# Barny: Arquitecto de Software y Asistente de Desarrollo

Bienvenido al repositorio oficial de **Barny**, un agente autónomo avanzado diseñado para potenciar y validar el desarrollo de software. Este agente ha sido desarrollado bajo los requerimientos de la "Actividad 8 P Web" y extendido significativamente para cumplir con un perfil de Arquitecto Senior y evaluador experto en calidad.

## 🎯 Objetivo del Agente
Barny no es solo un generador de código, es un mentor y arquitecto técnico. Su objetivo es:
1. **Analizar rigurosamente** los requerimientos y detectar ambigüedades antes de escribir código (arquitectura *Plan & Act*).
2. **Revisar código** validando principios de ingeniería de software (SOLID, KISS, DRY, Clean Code).
3. **Potenciar al desarrollador** proponiendo tareas estructuradas, casos de prueba (Given-When-Then), verificando manejo de errores y realizando análisis de seguridad básicos.

## 🚀 Instalación y Configuración

1. **Clona el repositorio:**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd Barny_agent
   ```

2. **Crea un entorno virtual (opcional pero recomendado):**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install google-genai python-dotenv
   ```

4. **Variables de entorno:**
   Crea un archivo llamado `.env` en la raíz del proyecto. Este archivo **NO** debe subirse a Git. Agrega tu clave de API:
   ```env
   GEMINI_API_KEY=tu_clave_api_aqui
   ```

## 🛠️ Herramientas Disponibles (Function Calling)

Barny está equipado con un ecosistema de 10 herramientas para evaluar y gestionar el desarrollo (Fase 7 y 12).
1. `analizar_requisitos`: Extrae requerimientos, restricciones y ambigüedades de un prompt.
2. `revisar_codigo`: Analiza legibilidad, DRY, KISS y responsabilidades.
3. `generar_pruebas`: Diseña casos de prueba correctos, incorrectos y límites.
4. `evaluar_solid`: Verifica cumplimiento estricto de SRP, OCP, LSP, ISP, DIP.
5. `validar_nombres`: Audita nombres de variables y funciones (Clean Code).
6. `analisis_seguridad_basico`: Busca vulnerabilidades OWASP (inyecciones, hardcoding).
7. `generar_checklist_calidad`: Produce una lista de verificación pre-entrega.
8. `detectar_code_smells`: Detecta funciones largas, parámetros excesivos o complejidad.
9. `planificar_tareas`: Desglosa grandes módulos en tareas pequeñas accionables.
10. `verificar_manejo_errores`: Comprueba la resiliencia del software ante fallos (try/catch).

## ▶️ Cómo ejecutarlo

Para interactuar con Barny, simplemente ejecuta:
```bash
python main.py
```

Escribe tu solicitud (ej. "Revisa este fragmento de código...") y Barny decidirá automáticamente qué herramientas invocar antes de darte su respuesta. Para salir, escribe `salir`.

## 🧪 Pruebas Realizadas
1. **Caso Correcto:** Se pidió a Barny estructurar un sistema de ventas. Barny detectó la falta de especificación técnica y utilizó la herramienta `analizar_requisitos` para requerir más información antes de escupir código a ciegas.
2. **Caso Ambiguo:** Se indicó "Haz un sistema completo". Barny invocó su regla de ambigüedades y solicitó contexto, evitando alucinaciones.
3. **Código Problemático:** Se le envió una función espagueti (muy larga). Barny utilizó `revisar_codigo`, `detectar_code_smells` y `evaluar_solid` para señalar violaciones al principio SRP.

## ⚠️ Limitaciones Conocidas
- Barny asume que estás usando Python 3.11+.
- La herramienta de análisis de seguridad es básica (búsqueda estática conceptual impulsada por LLM) y no reemplaza un SAST verdadero (ej. SonarQube).
- Depende completamente de la disponibilidad de la API de Google Gemini y su cuota.

## 🌟 Mejoras Personales (Fase 12)
Para superar el mínimo esperado, se implementó lo siguiente:
- **7 herramientas adicionales:** En lugar de 3, Barny cuenta con 10. Se agregaron validadores explícitos para SOLID, Nombres, Code Smells, Seguridad, Manejo de errores y Checklist.
- **Ciclo Agéntico Plan & Act:** El prompt se diseñó estructuralmente para prohibirle a Barny codificar sin pensar primero, forzando un paso de análisis y planeación.
- **Manejo Integral de Errores:** La interfaz CLI en `main.py` ahora captura `google.genai.errors.APIError` de forma específica, brindando mensajes de error más limpios (ej. cuota agotada) sin romper el terminal con stack traces.
