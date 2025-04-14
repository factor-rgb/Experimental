from django.shortcuts import render, redirect
from .models import Agenda,Horarios
from .forms import AgendaForm,HorariosForm


def index(request):
      return render(request, "core/index.html")

def mes(request):
      query = Agenda.objects.all()
      query2 = Horarios.objects.all()
      if request.method == 'GET':
            form_agenda = AgendaForm()
            context = {'form_agenda': form_agenda, 'fechas': query, 'horas': query2}
            return render(request, 'core/meses.html', context)
      else:
            form = AgendaForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect('core:meses')

def prueba(request):
     return render(request, "core/selectable.html")

def borrar_evento(request, pk):
      query = Agenda.objects.get(id=pk)
      if request.method == 'POST':
            query.delete()
            return redirect('core:meses')
      return render(request, 'core/confirmacion.html', {'object': query})

def crear_asunto(request):
      if request.method == 'GET':
            form_horario = HorariosForm()
            context = {'form_horario': form_horario}
            return render(request, 'core/horarios_form.html', context)
      else:
            form = HorariosForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect('core:crear_asunto')
