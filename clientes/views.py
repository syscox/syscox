from django.shortcuts import render
from clientes.forms import ClienteForm


def index(request):
    return render(request, 'clientes/index.html')


def cliente_nuevo(request):
    clienteF = ClienteForm

    if request.POST:
        clienteF = ClienteForm(request.POST or None)
        if clienteF.is_valid():
            obj = clienteF.save(commit=False)
            obj.save()
    context = {"cliente": clienteF,
               }
    return render(request, 'clientes/cliente_nuevo.html', context)
