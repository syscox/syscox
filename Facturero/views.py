from django.shortcuts import render
from django.contrib.auth.models import User


def index(request):
    usuario = 'desconocido'
    if User.is_authenticated:
        usuario = User
    context = {
        "donde_estoy": 'INICIO',
        "usuario": usuario.username

    }
    return render(request, 'base.html', context)
