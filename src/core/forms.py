from django import forms

from .models import Agenda


class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = "__all__"
        widgets = {'fecha_inicio': forms.DateInput(attrs={"type": "date"}),
                   'fecha_final': forms.DateInput(attrs={"type": "date"}),
                   }