from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template = 'index.html'
    context = {
        'pregunta': 'kiere magia prro?',
        'magia': 'toma tus momos :V'
    }

    return render(request, template, context)
