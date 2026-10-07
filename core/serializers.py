from rest_framework import serializers
from .models import Registro

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        # OBLIGATORIO: Se incluye el "id" y todos los campos de tu modelo[cite: 19]
        fields = [
            "id", 
            "nombre", 
            "edad", 
            "cupos", 
            "estado", 
            "motivo", 
            "fecha", 
            "eliminado", 
            "fecha_eliminacion"
        ]
        
        # SEGURIDAD: Solo permitimos que el cliente escriba nombre, edad y cupos. 
        # El resto lo calcula tu sistema[cite: 19].
        read_only_fields = [
            "estado", 
            "motivo", 
            "fecha", 
            "eliminado", 
            "fecha_eliminacion"
        ]

    # Validación personalizada (evita que un piloto ponga edad negativa)[cite: 19]
    def validate_edad(self, valor):
        if valor < 0:
            raise serializers.ValidationError("La edad no puede ser negativa")
        return valor