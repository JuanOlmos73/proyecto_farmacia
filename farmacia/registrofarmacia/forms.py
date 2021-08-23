from django import forms
from django.db.models import fields
from django.forms.widgets import ClearableFileInput
from .models import medicamentos
from .models import salida_medicamento
'''from .models import salida_medicamento'''

class CustomClearableFileInput(ClearableFileInput):

    template_with_clear = '<br> <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'

class Medicamentoforms(forms.ModelForm):
    class Meta:
        model = medicamentos
        fields = ['imagen','clave','nombre','cantidad','fecha_de_caducidad','descripcion','disponibilidad']
        widgets = {
                'imagen' : ClearableFileInput
        }

        
class editarforms(forms.ModelForm):
    class Meta:
        model=medicamentos
        fields=['cantidad']

class salidaFarmacoforms(forms.ModelForm):
    class Meta:
        model = salida_medicamento
        fields = ['nombre_paciente','medicamento','cantidad_suministrada','fecha_suministrada']