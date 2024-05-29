from django.urls import path
from secretariaPersonal import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.personal, name="Personal"),
    path('registrarPersonal/', views.registrarPersonal, name="registrarPersonal"),
    path('editarPersonal/<int:id>', views.editarPersonal, name='editarPersonal'),
    path('elimarPersonal/<int:id>', views.eliminarPersonal, name="eliminarPersonal"),
    ]