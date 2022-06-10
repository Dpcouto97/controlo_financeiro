from django.urls import path
from .view_tipodespesa import tipodespesa_registo_view, tipodespesa_lista_view, tipodespesa_detalhes_view, tipodespesa_elimina_view

urlpatterns = [
    path('registo/', tipodespesa_registo_view, name='tipodespesa-registo-view'),
    path('lista/', tipodespesa_lista_view, name='tipodespesa-lista-view'),
    path('detalhes/<int:my_id>/', tipodespesa_detalhes_view, name='tipodespesa-detalhes-view'),
    #path('atualizar/<int:my_id>/', tipodespesa_edit_view, name='tipodespesa_edit_view'),
    path('eliminar/<int:my_id>/', tipodespesa_elimina_view, name='tipodespesa-elimina-view'),
]