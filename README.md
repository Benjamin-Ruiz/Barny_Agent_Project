# Barny: Arquitecto de Software y Asistente de Desarrollo

Bienvenido al repositorio oficial de **Barny**, un agente autónomo avanzado diseñado para potenciar y validar el desarrollo de software. Este agente ha sido desarrollado para cumplir con un perfil de Arquitecto Senior y evaluador experto en calidad.

## Objetivo del Agente
1. **Analisis rigutoso:** Analiza los requerimientos y detecta ambigüedades antes de escribir código 
2. **Rrevision de codigo:** Valida principios de ingeniería de software como SOLID, KISS, DRY y Clean Code.
3. **Asistencia al desarrollador:** Propone tareas estructuradas, casos de prueba, verificando manejo de errores y realizando análisis de seguridad básicos.

## Instalación y Configuración

1. **Clona el repositorio:**

## Herramientas Disponibles (Function Calling)

Barny está equipado con 10 herramientas para evaluar y gestionar el desarrollo.
1. `analizar_requisitos`: Extrae requerimientos, restricciones y ambigüedades de un prompt.
2. `revisar_codigo`: Analiza legibilidad, DRY, KISS y responsabilidades.
3. `generar_pruebas`: Diseña casos de prueba correctos, incorrectos y límites.
4. `evaluar_solid`: Verifica cumplimiento estricto de SRP, OCP, LSP, ISP, DIP.
5. `validar_nombres`: Audita nombres de variables y funciones (Clean Code).
6. `analisis_seguridad_basico`: Busca vulnerabilidades OWASP.
7. `generar_checklist_calidad`: Produce una lista de verificación pre-entrega.
8. `detectar_code_smells`: Detecta funciones largas, parámetros excesivos o complejidad.
9. `planificar_tareas`: Desglosa grandes módulos en tareas pequeñas accionables.
10. `verificar_manejo_errores`: Comprueba la resiliencia del software ante fallos.

## ¿Cómo ejecutarlo?

Para interactuar con Barny, simplemente ejecuta:
```bash
python main.py
```
Escribe tu solicitud (ej. "Revisa este fragmento de código...") y Barny decidirá automáticamente qué herramientas invocar antes de darte su respuesta. Para salir, escribe `salir`.

## Pruebas Realizadas
1. **Caso Correcto:** 
2. **Caso Ambiguo:** 
3. **Código Problemático:** 

## Limitaciones Conocidas
- Se debe utilizar Python 3.11+.
- Depende completamente de la disponibilidad de la API de Google Gemini y su cuota.

