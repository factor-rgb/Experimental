from django.shortcuts import render, redirect
from .models import Agenda
from .forms import AgendaForm


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

def borrar_evento(request, pk):
      query = Agenda.objects.get(id=pk)
      if request.method == 'POST':
            query.delete()
            return redirect('core:meses')
      return render(request, 'core/confirmacion.html', {'object': query})
