from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Despesa, TipoDespesa, Receita
from .forms import TipoDespesaRegistoForm


def tipodespesa_registo_view(request):
    form = TipoDespesaRegistoForm(request.POST or None)
    print(request.user.id)
    if form.is_valid():
        form.instance.user = request.user.id
        form.save()
        return HttpResponseRedirect(reverse('tipodespesa-lista-view'))
    else:
        print(form.errors)

    return render(request, "tipodespesa/tipodespesa_registo.html", {'form': form})


def tipodespesa_lista_view(request):
    tipodespesas = TipoDespesa.objects.filter(user=request.user.id)
    return render(request, "tipodespesa/tipodespesa_lista.html", {"tipodespesa_lista": tipodespesas})


def tipodespesa_detalhes_view(request, my_id):
    tipodespesa = get_object_or_404(TipoDespesa, id=my_id)
    return render(request, "tipodespesa/tipodespesa_detalhes.html", {"tipodespesa": tipodespesa})


def tipodespesa_atualiza_view(request, my_id):
    siem = get_object_or_404(Siem, id=my_id)
    form = SiemRegisterForm(request.POST or None, instance=siem)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('siem-list-view'))
    return render(request, "siems/siem_update.html", {'form': form})


def tipodespesa_elimina_view(request, my_id):
    tipodespesa = get_object_or_404(TipoDespesa, id=my_id)

    #Checka se o tipo de despesa tem despesas associadas, porque as depesas obrigatoriamente tem que ter um tipo de despesa!
    #Portanto a logica sera ter um botao para o utilizador escolher se realmente quer eliminar o tipo de despesa, informo
    #que todas as depesas associadas serao eliminadas! No maximo pode-se alterar as despesas para outro tipo de despesa e eliminar esse tipo de despesa.
    flag = False
    if len(tipodespesa.despesa_set.filter(user=request.user.id)) != 0:
        flag = True

    if request.method == "POST":
        tipodespesa.delete()
        return HttpResponseRedirect(reverse('tipodespesa-lista-view'))
    return render(request, "tipodespesa/tipodespesa_elimina.html", {"tipodespesa":tipodespesa, "flag": flag})