from django.urls import path
from secretariaAcudiente import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.acudiente, name="Acudiente"),
    path('acudiente/<int:acudiente_id>/', views.acudiente_detalle, name='acudiente_detalle'),
    path('registrarAcudiente/', views.registrarAcudiente, name="registrarAcudiente"),
    path('editarAcudiente/<int:id>', views.editarAcudiente, name="editarAcudiente"),
    path('eliminarAcudiente/<int:id>', views.eliminarAcudiente, name="eliminarAcudiente"),
    ]