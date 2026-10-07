def decidir(edad, cupos, nombre="Pilotos"):
    estado = ""
    motivo = ""

    if edad < 0 or cupos < 0:
        estado = "invalido"
        motivo = "La edad y los cupos no pueden ser negativos."
    elif edad < 18:
        estado = "rechazado"
        motivo = "El piloto es menor de 18 años."
    elif cupos == 0:
        estado = "rechazado"
        motivo = "No quedan cupos disponibles."
    else:
        estado = "aceptado"
        motivo = f"{nombre} cumple los requisitos y existe un cupo disponible."

    return estado,motivo



    
        


