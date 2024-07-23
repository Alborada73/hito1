from django.contrib import admin
from .models import Tipo_usuario, Usuario, Tipo_inmueble, Region, Comuna, Inmueble

# Register your models here.
admin.site.register(Tipo_usuario)
admin.site.register(Usuario)
admin.site.register(Tipo_inmueble)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Inmueble)
