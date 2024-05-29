from django.contrib import admin
from .models import Personal, Cargo

# Register your models here.

class adminPersonal(admin.ModelAdmin):
    readonly_fields=("created", "updated")
    
admin.site.register(Personal, adminPersonal)
admin.site.register(Cargo)