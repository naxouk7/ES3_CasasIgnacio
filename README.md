# API de Registros - Evaluación 3
**Alumno:** Ignacio Casas

## Justificación de Configuración (REST_FRAMEWORK)
Elegí `TokenAuthentication` en lugar de sesiones con cookies porque una API está pensada para ser consumida por otros programas (sin navegador), los cuales deben identificarse enviando su credencial en la cabecera de cada petición. Además, establecí el `PAGE_SIZE` en 10 para garantizar un rendimiento estable y no sobrecargar la respuesta JSON en caso de que la tabla de registros crezca masivamente.

## Tabla de Endpoints

| Verbo HTTP | Endpoint | Descripción de la Acción |
|---|---|---|
| **POST** | `/api/token/` | Genera y entrega el token de autenticación del usuario. |
| **GET** | `/api/registros/` | Lista todos los registros activos ordenados por fecha. |
| **POST** | `/api/registros/` | Crea un registro evaluando automáticamente los cupos y la edad. |
| **GET** | `/api/registros/<id>/` | Muestra el detalle de un registro específico. |
| **PUT/PATCH** | `/api/registros/<id>/` | Actualiza los datos permitidos de un registro. |
| **DELETE** | `/api/registros/<id>/` | Borrado lógico del registro (Restringido solo a usuarios Staff). |