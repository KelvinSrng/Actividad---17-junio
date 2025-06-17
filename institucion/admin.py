from django.contrib import admin
from institucion.models import *

# Register your models here.

admin.site.register(Departamento)
admin.site.register(Instructor)
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Inscripcion)
admin.site.register(Tarea)
admin.site.register(Entrega)