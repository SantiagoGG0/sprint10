from django import forms
from .models import Mascota, Propietario

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'

class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = '__all__'