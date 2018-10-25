from django.shortcuts import render
from .models import Post


def index(request):
    return render(request, 'blog/index.html',)

def mascotas(request):
    return render(request, 'blog/mascotas.html',)
def nosotros(request):
    return render(request, 'blog/nosotros.html',)
def adopta(request):
    return render(request, 'blog/adopta.html',)
def contacto(request):
    return render(request, 'blog/contacto.html',)
# Create your views here.