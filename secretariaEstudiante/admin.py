from django.contrib import admin
from .models import document, sede, estudiante, curso

# Register your models here.

class adminEstudiante(admin.ModelAdmin):
    readonly_fields=("created","updated")

admin.site.register(document)
admin.site.register(sede)
admin.site.register(curso)
admin.site.register(estudiante, adminEstudiante)