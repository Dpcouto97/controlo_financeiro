#The forms.py is where we should add the extra validations that we want to apply to the input forms income data/info
from django import forms
from django.core.exceptions import ValidationError
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Despesa, TipoDespesa, Receita


class TipoDespesaRegistoForm(forms.ModelForm):
    nome = forms.CharField(label=False, widget=forms.TextInput(attrs={"placeholder": "Nome"}), required=True)
    descricao = forms.CharField(label=False, widget=forms.TextInput(attrs={"placeholder": "Descricao"}), required=True)
    valor_normal = forms.DecimalField(label=False, widget=forms.TextInput(attrs={"placeholder": "Formato: 2.00"}))
    user = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = TipoDespesa
        fields = [
            'nome',
            'descricao',
            'valor_normal',
            'user'
        ]


class DespesaRegistoForm(forms.ModelForm):
    # Has to be forms.ModelForm, otherwise we cant use form.save() in the view
    nome = forms.CharField(label=False, widget=forms.TextInput(attrs={"placeholder": "Nome"}), required=True)
    descricao = forms.CharField(label=False, widget=forms.TextInput(attrs={"placeholder": "Descricao"}), required=True)
    valor = forms.DecimalField(label=False, widget=forms.TextInput(attrs={"placeholder": "Formato: 2.00"}))
    user = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    tipo_despesa = forms.ModelChoiceField(queryset=TipoDespesa.objects.all(), label=False, required=True)


    class Meta:
        model = Despesa
        fields = [
            'nome',
            'descricao',
            'valor',
            'user',
            'tipo_despesa'
        ]


class ReceitaForm(forms.ModelForm):
    nome = forms.CharField(label=False, widget=forms.TextInput(attrs={"placeholder": "Name"}), required=True)
    descricao = forms.CharField(label=False, widget=forms.TextInput(attrs={"placeholder": "Description"}), required=True)

    class Meta:
        model = Receita
        fields = [
            'nome',
            'descricao'
        ]