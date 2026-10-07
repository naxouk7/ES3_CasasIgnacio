import os
import django
from decouple import config

# Esto prepara a Django para que el script pueda funcionar por sí solo
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miproyecto.settings')
django.setup()

from django.contrib.auth.models import User, Group

# 1. Creamos los tres roles
for nombre in ("admin", "normal", "viewer"):
    Group.objects.get_or_create(name=nombre)

# 2. Creamos al usuario "lector". La contraseña sale del .env, NO escrita aquí
# Si el usuario ya existe, evitamos que dé error
if not User.objects.filter(username="lector").exists():
    u = User.objects.create_user("lector", password=config("PASS_LECTOR"))
    u.groups.add(Group.objects.get(name="viewer"))
    print("Roles y usuario 'lector' creados con éxito.")
else:
    print("Los roles ya existen y el usuario 'lector' ya estaba creado.")