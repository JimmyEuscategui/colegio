from django.forms import ModelForm
from .models import Personal

class PersonalForm(ModelForm):
    class Meta:
        model = Personal
        fields = '__all__'
        
    