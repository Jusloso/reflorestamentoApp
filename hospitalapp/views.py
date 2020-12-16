from django.shortcuts import *
from django.http import HttpResponse
from .forms import Florestaform
from .models import Floresta
from django.http import HttpResponse
from  django.shortcuts import get_list_or_404, get_object_or_404, render
from django import *
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'hospital/index.html')

def florestas(request):
    #return HttpResponse("<h1> Aqui é a área de hospital<h1>")
    florestas = Floresta.objects.all()
    busca = request.GET.get('search')
    if busca:
        florestas = Floresta.objects.filter(estado__icontains = busca)
    return render(request, 'hospital/florestas.html', {'florestas':florestas})


def editar(request, id):
    hosp = get_object_or_404(Floresta, pk=id)
    form = Florestaform(instance=hosp)

    if(request.method == "POST"):
        form=Florestaform(request.POST, request.FILES, instance=hosp)

        if form.is_valid():
            form.save()
            return redirect('florestas')

        else:

            return render(request, "hospital/editar_floresta.html",{'form':form, 'hosp':hosp})
    else:
        return render(request, "hospital/editar_floresta.html",{'form':form, 'hosp':hosp})


def criar_floresta (request):
    form = Florestaform(request.POST)
    if request.method == "POST":
        form = Florestaform(request.POST, request.FILES)
        if form.is_valid():
            hosp = form.save()
            hosp.save()
            messages.success(request, 'Floresta adicionada com sucesso!')
            form = Florestaform()
    return render(request, 'hospital/criar_floresta.html', {'form':form})


def deletar(request, id):
    hosp = get_object_or_404(Floresta, pk=id)
    if request.method == "POST":
        hosp.delete()
        return redirect('florestas')
    return render(request, "hospital/deletar_floresta.html", {'hosp':hosp})