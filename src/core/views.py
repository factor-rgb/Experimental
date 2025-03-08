from django.shortcuts import render
from .models import Agenda
from .forms import AgendaForm

from django.views.generic import CreateView
from django.urls import reverse_lazy


def index(request):
      query = Agenda.objects.all()
      context = {"fechas": query}
      return render(request, "core/index.html", context)

class AgendaCreateView(CreateView):
    model = Agenda
    form_class = AgendaForm
    success_url = reverse_lazy('core:index')