from django.shortcuts import render
# from django.contrib.auth.models import User


def index(request):
    context = {
        "donde_estoy": 'INICIO',

    }
    return render(request, 'base.html', context)
