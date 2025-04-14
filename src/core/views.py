from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from django.shortcuts import render, redirect
from .models import Agenda,Horarios
from .forms import AgendaForm,HorariosForm


def index(request):
      return render(request, "core/index.html")

def mes(request):
      query = Agenda.objects.all()
      query2 = Horarios.objects.all()
      if request.method == 'GET':
            form = HorariosForm()
            context = {'form': form, 'fechas': query, 'horas': query2}
            return render(request, 'core/meses.html', context)
      else:
            form = HorariosForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect('core:meses')
      
def borrar_asunto(request, pk):
      query = Horarios.objects.get(id=pk)
      if request.method == 'POST':
            query.delete()
            return redirect('core:meses')
      return render(request, 'core/confirmacion.html', {'object': query})

class AgendaCreateView(CreateView):
    model = Agenda
    form_class = AgendaForm
    success_url = reverse_lazy('core:meses')


class AgendaUpdateView(UpdateView):
    model = Agenda
    form_class = AgendaForm
    success_url = reverse_lazy('core:meses')

class AgendaDeleteView(DeleteView):
    model = Agenda
    success_url = reverse_lazy('core:meses')
