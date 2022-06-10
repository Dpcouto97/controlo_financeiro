from django.urls import path
from .view_despesa import despesa_registo_view, despesa_detalhes_view, despesa_lista_view, despesa_atualiza_view, despesa_elimina_view

urlpatterns = [
    path('registo/', despesa_registo_view, name='despesa-registo-view'),
    #path('lista/', despesa_lista_view='despesa_lista_view'),
    #path('detalhes/<int:my_id>/', despesa_detalhes_view, name='despesa_detalhes_view'),
    #path('atualizar/<int:my_id>/', despesa_atualiza_view, name='despesa_atualiza_view'),
    #path('eliminar/<int:my_id>/', despesa_elimina_view, name='despesa_elimina_view'),
]