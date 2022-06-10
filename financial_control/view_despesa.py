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
    else:
        print(form.errors)

    return render(request, "despesa/despesa_registo.html", {'form': form})


def despesa_lista_view(request):
    siems = Siem.objects.all()
    return render(request, "siems/siem_list.html", {"siems_list": siems})


def despesa_detalhes_view(request, my_id):
    siem = get_object_or_404(Siem, id=my_id)
    return render(request, "siems/siem_details.html", {"siem": siem})


def despesa_atualiza_view(request, my_id):
    siem = get_object_or_404(Siem, id=my_id)
    form = SiemRegisterForm(request.POST or None, instance=siem)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('siem-list-view'))
    return render(request, "siems/siem_update.html", {'form': form})


def despesa_elimina_view(request, my_id):
    siem = get_object_or_404(Siem, id=my_id)

    #Checks if the SIEM has clients associated, if yes than flag = True.
    flag = False
    if len(siem.client_set.all()) !=0:
        flag = True

    if request.method == "POST":
        siem.delete()
        return HttpResponseRedirect(reverse('siem-list-view'))
    return render(request, "siems/siem_delete.html", {"siem": siem, "flag": flag})