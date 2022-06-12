from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Despesa, TipoDespesa, Receita
from .forms import DespesaRegistoForm


def despesa_registo_view(request):
    tipodespesa = TipoDespesa.objects.filter(user=request.user.id)
    if not tipodespesa:
        return render(request, "despesa/despesa_registo_invalido.html")

    form = DespesaRegistoForm(request.POST or None)
    if form.is_valid():
        form.instance.user = request.user.id
        form.save()
        return HttpResponseRedirect(reverse('despesa-lista-view'))
    else:
        print(form.errors)

    return render(request, "despesa/despesa_registo.html", {'form': form})


def despesa_lista_view(request):
    despesas = Despesa.objects.filter(user=request.user.id)
    return render(request, "despesa/despesa_lista.html", {"despesa_lista": despesas})


def despesa_detalhes_view(request, my_id):
    despesa = get_object_or_404(Despesa, id=my_id)
    return render(request, "despesa/despesa_detalhes.html", {"despesa": despesa})


def despesa_atualiza_view(request, my_id):
    despesa = get_object_or_404(Despesa, id=my_id)
    form = DespesaRegistoForm(request.POST or None, instance=despesa)
    if form.is_valid():
        form.instance.user = request.user.id
        form.save()
        return HttpResponseRedirect(reverse('despesa-lista-view'))
    return render(request, "despesa/despesa_atualiza.html", {'form': form, "despesa": despesa})


def despesa_elimina_view(request, my_id):
    despesa = get_object_or_404(Despesa, id=my_id)

    if request.method == "POST":
        despesa.delete()
        return HttpResponseRedirect(reverse('despesa-lista-view'))
    return render(request, "despesa/despesa_elimina.html", {"despesa":despesa})