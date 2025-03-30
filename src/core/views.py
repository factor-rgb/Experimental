from django.shortcuts import render, redirect
from .models import Agenda
from .forms import AgendaForm

from django.views.generic import CreateView
from django.urls import reverse_lazy


def index(request):
      query = Agenda.objects.all()
      context = {"fechas": query}
      return render(request, "core/index.html", context)

def mes(request):
      query = Agenda.objects.all()
      if request.method == 'GET':
            form = AgendaForm()
            context = {'form': form, 'fechas': query}
            return render(request, 'core/meses.html', context)
      else:
            form = AgendaForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect('core:mes')

def prueba(request):
     return render(request, "core/selectable.html")