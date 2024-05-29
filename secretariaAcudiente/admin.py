from django.contrib import admin
from .models import Acudiente

# Register your models here.

class adminAcudiente(admin.ModelAdmin):
    readonly_fields=("created","updated")
    
admin.site.register(Acudiente, adminAcudiente)