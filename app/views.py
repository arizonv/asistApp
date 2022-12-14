from django.shortcuts import render




def index(request):
    return render(request, 'index.html')


def indexHub(request):
    return render(request, 'indexHub.html')


def indexDuoc(request):
    return render(request, 'indexDuoc.html')


def contacto(request):
    return render(request, 'contacto.html')

