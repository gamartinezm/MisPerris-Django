from django import forms
from .models import Mascota

class MascotaForm(forms.ModelForm):

	class meta:
		model = Mascota
		fields = ('nombre','raza','descripcion','estado',)
