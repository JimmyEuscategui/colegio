from django.forms import ModelForm
from .models import Acudiente

class AcudienteForm(ModelForm):
    class Meta:
        model = Acudiente
        fields = '__all__'