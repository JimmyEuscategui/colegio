from django.urls import path
from secretaria import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Home"),
    path('personal/', views.personal, name="Personal"),
    path('acudiente/', views.acudiente, name="Acudiente"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)