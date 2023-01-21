from django.contrib import admin

from .models import Asignatura, Imparte, Profesor,Carreras,Estudiantes,Inscribe,Salon,Asociado

admin.site.register(Profesor)
admin.site.register(Asignatura)
admin.site.register(Carreras)
admin.site.register(Estudiantes)
admin.site.register(Imparte)
admin.site.register(Inscribe)
admin.site.register(Salon)
admin.site.register(Asociado)

