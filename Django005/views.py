from django.shortcuts import render, redirect, get_object_or_404
from Cliente.models import Cliente
from Cliente.forms import ClienteForm


def home(request):
    return render(request, 'home.html')


def read_cliente(request):
    Clientes = Cliente.objects.all()
    return render(request, 'read_cliente.html', {'Clientes': Clientes})

def create_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('read_cliente')
    else:
        return render(request, 'create_cliente.html', {'form': form})

def update_cliente(request, id):
    client = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect('read_cliente')
    else:
        return render(request, 'update_cliente.html',{'form': form})

def delete_cliente(request, id):
    client = get_object_or_404(Cliente, pk=id)
    client.delete()
    return redirect('read_cliente')