#01 ¿Que herramienta de IA usaste y para que la consultaste?

Utilice CHATGPT en la etapa inicial para revisar ideas y estructurar el apartado de negocio y tecnico de mi archivo, Posteriormente utilice Gemini como asistente de depuracion de errores durante la programacion en Python y la configuracion de Django.

La IA funciono como un apoyo para interpretar los avisos de la consola, dejandome a mi la responsabilidad de armar la logica del proyecto y gestionar correctamente la ubicacion de los archivos

#02 ¿CONSULTA CONCRETA Y RESPUESTA RECIBIDA?

Durante el desarrollo de la vista de Django al intentar levantar el servidor, la aplicacion fallo arrojando un texto largo de error. Le copie el bloque completo a la IA. Me respondio identificando que el problema de raiz era un SyntaxError: unterminated string literal en mi archivo views.py, explicandome de forma sencilla que el codigo fallaba porque faltaba tipear una comilla de apertura

#03

En otro paso, la IA me indicio ejecutar directamente el comando para encender el servidor, pero la terminal me arrojo el mensaje de error [Errno 2] No such file or directory indicando que no encontraba el ejecutable. La respuesta de la IA estaba incompleta porque asumia por defecto que mi terminal ya estaba posicionada en la carpeta interior del proyecto. Tuve que analizar estructura de mis carpetas en el editor, aplicar mi propio criterio para deducir que estaba en un nivel mas arriba.

EVALUACION #02

Herramienta utilizada: Gemini
¿Como aplico el sistema de roles y protejo las vistas con decoradores sin guardar contraseñas en mi modelo?

La IA me entrego el codigo base, pero tuve que corregir un error de sintaxis que genero en urls.py (le falto una comilla al escribir name="logout") y tuve que deducir y mover manualmente el script crear_usuarios.py a la carpeta correcta