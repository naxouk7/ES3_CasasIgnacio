from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.api_views import RegistroViewSet
# Importamos la herramienta para generar tokens
from rest_framework.authtoken.views import obtain_auth_token 

router = DefaultRouter()
router.register(r"registros", RegistroViewSet, basename="registro")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("api/", include(router.urls)),
    
    # NUEVA RUTA: Aquí es donde pediremos la llave de acceso
    path("api/token/", obtain_auth_token, name="api_token"),
    
    # La ruta de tus HTML sigue apagada temporalmente
    # path("", include("core.urls")), 
]