#Sistema de Inscripcion a una Carrera

1. NEGOCIO

#Problema

El proceso de inscripcion de pilotos a un evento de automovilismo puede requrir revisar manualmente si cada participantes cumple los requisitos establecidos y si todavia existen cupos disponibles. Esto puede generar errores o aceptar solicitudes que no cumplen las condiciones.

#Solucion 

Se desarrollara un sistema de inscripcion que permita ingresar los datos de un piloto y determinar automaticamente si puede participar en la carrera. El sitema verificara la edad del piloto y los cupos disponibles, informando el resultado y el motivo cuando la inscripcion sea rechazada

#Alcance

El sistema permitira ingresar el nombre del piloto, su edad y la cantidad de cupos disponibles. Validara los datos, determinara el resultado de la inscripcion, mostrara el motivo correspondiente y guardara los registros en un archivo JSON. Posteriormente, los registros seran mostrados en una tabla mediante la consola y en una pantalla web desarrollada con Django.

En esta version se utiliza SQLite, incluyendo las 4 operaciones CRUD y incorporando roles de usuario (admin, normal, viewer) utilizando un sistema de borrado logico

#Priorizacion MoSCoW

Mus-Imprescindible
-. Solicitar los datos del piloto
-. Validar los datos ingresados
-. Determinar uno de los cuatro resultados posibles
-. Mostrar el resultado y su motivo
-. Guardar los registros en datos.json
-. Mostrar los registros utilizando tabulate
-. Mostrar los registros mediante una pagina web en Django
-. Sistema de ususaris y contraseñas
-. Base de datos

Should- Importante
-. Permite modificar una inscripcion
-. Evitar que un mismo piloto se registre dos veces

Could- Deseable
-. Buscar un piloto por nombre
-. Mostrar estadisticas de las inscripciones
-. Exportar los registros a Excel

Won´t- Fuera de esta version
-. Sistema de pagos
-. API
-. Gestion completa de un campeonato

2. TECNICO

#Datos de entrada

El programa solicitara los siguientes datos

-. Nombre del piloto: texto (str)
-. Edad del piloto: numero entero (int)
-. Cupos disponibles: numero entero (int)

Los valores de la edad y cupos seran convertidos a numero enteros para poder realizar las comparaciones necesarias

#Regla de decision

El programa evaluara los datos en el siguiente orden:

1-. Datos Invalidos: ocurre cuando la edad o la cantidad de cupos es negativa
2-. Rechazado por edad: ocurre cuando los datos son validos, pero el piloto tiene menos de 18 años
3-. Rechazado por falta de cupos: ocurre cuando el piloto tiene 18 años o mas, pero no quedan cupos disponibles
4-. Aceptado: ocurre cuando el piloto tiene 18 años o mas y existe al menos un cupo disponible

#Paquete externo

Se utilizara el paquete externo tabulate, instalado mediante pip, para mostrar los registros guardados en forma de tabla en la consola

#Pantalla web

El proyecto tendra una sola pantalla web accesible desde la direccion /. Esta pantalla mostrara un resumen de las inscripciones almacenadas en datos.json, incluyendo los datos del piloto, el resultado de la inscripcion y el motivo correspondiente

La aplicacion sera desarrollada con Django y no utilizara una base de datos



