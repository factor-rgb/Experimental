from django import forms

from .models import Agenda, Horarios


class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = "__all__"
        widgets = {'fecha_inicio': forms.DateInput(attrs={"type": "date"}),
                   'fecha_final': forms.DateInput(attrs={"type": "date"}),
                   }
        
class HorariosForm(forms.ModelForm):
    class Meta:
        model = Horarios
        fields = "__all__"
        widgets = {'hora': forms.DateTimeInput(attrs={"type": "datetime-local"})}