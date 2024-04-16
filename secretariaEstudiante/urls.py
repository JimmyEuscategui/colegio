from django.urls import path
from secretariaEstudiante import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.estudiente, name="Estudiante"),
    path('createEstudiante/', views.createEstudiante, name="createEstudiante"),
    path('editarEstudiante/<int:id>', views.editarEstudiante, name="editarEstudiante"),
    path('eliminarEstudiante/<int:id>', views.eliminarEstudiante, name="eliminarEstudiante"),
    ]