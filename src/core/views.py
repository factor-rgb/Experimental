from django.shortcuts import render


def pruebas(request):
    return render(request, 'core/index.html')
