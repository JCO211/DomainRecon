# DomainRecon
Herramienta OSINT básica creada en Kali Linux para reconocimiento de dominios.

DomainRecon es una herramienta de reconocimiento (recon) diseñada para especialistas en ciberseguridad y entusiastas de OSINT (Open Source Intelligence). Su objetivo principal es mapear la presencia digital de un dominio de forma rápida y automatizada.
🔍 Función Exacta

El script automatiza tres tareas críticas durante la fase de reconocimiento de una auditoría:

    Resolución DNS Directa: Identifica la dirección IP pública del dominio principal proporcionado, permitiendo conocer el servidor que aloja la web central.

    Fuerza Bruta de Subdominios: El script prueba una lista de nombres comunes (como dev, mail, admin, api) ante el dominio objetivo. Esto sirve para descubrir activos ocultos o mal configurados que no aparecen en búsquedas convencionales.

    Generación de Reportes Automática: En lugar de perder datos en el historial de la terminal, la herramienta exporta cada hallazgo a un archivo de texto (.txt) con marca de tiempo y nombre del objetivo, facilitando la creación de informes de vulnerabilidades posteriores.

🚀 Cómo se usa (Instrucciones de uso)

1. Preparar el entorno: Asegurarse de tener Python y las dependencias instaladas:
Bash

pip install colorama requests

2. Ejecución básica: Desde la terminal, se ejecuta indicando el dominio al final del comando:
Bash

python3 domain_recon.py <dominio_objetivo>

Ejemplo: python3 domain_recon.py empresa.com

3. Análisis de Resultados:

    En pantalla: Verá un banner ASCII elegante con los resultados coloreados (Verde para hallazgos, Rojo para errores).

    En archivo: El script generará un archivo llamado reporte_empresa.com.txt en la misma carpeta, listo para ser revisado o enviado.

   ADJUNTO IMAGEN

   
<img width="1366" height="643" alt="Untitled" src="https://github.com/user-attachments/assets/fc3d0420-c890-472f-bc71-8e1e96e3a2be" />

