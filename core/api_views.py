from rest_framework import viewsets
from .models import Registro
from .serializers import RegistroSerializer
from .permissions import SoloStaffBorra # Importamos tu nuevo escudo de seguridad

class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.filter(eliminado=False).order_by("-fecha")
    serializer_class = RegistroSerializer
    
    # CONECTAMOS EL PERMISO: Todos leen/crean, solo el staff borra[cite: 15]
    permission_classes = [SoloStaffBorra]

    def perform_create(self, serializer):
        """El estado y motivo NO vienen del cliente: los decide el sistema."""
        edad = serializer.validated_data.get("edad")
        cupos = serializer.validated_data.get("cupos")
        
        # Regla de decisión automática incorporada
        if edad >= 18 and cupos > 0:
            estado_final = "aceptado"
            motivo_final = "Piloto habilitado para correr"
        elif edad < 18:
            estado_final = "rechazado"
            motivo_final = "Es menor de edad"
        else:
            estado_final = "rechazado"
            motivo_final = "No quedan cupos disponibles"
            
        # Guarda el registro forzando los campos automáticos
        serializer.save(estado=estado_final, motivo=motivo_final)