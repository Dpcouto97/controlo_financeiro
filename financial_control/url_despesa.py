from django.urls import path
from .view_despesa import despesa_registo_view, despesa_detalhes_view, despesa_lista_view, despesa_atualiza_view, despesa_elimina_view

urlpatterns = [
    path('registo/', despesa_registo_view, name='despesa-registo-view'),
    path('lista/', despesa_lista_view, name='despesa-lista-view'),
    path('detalhes/<int:my_id>/', despesa_detalhes_view, name='despesa-detalhes-view'),
    path('atualizar/<int:my_id>/', despesa_atualiza_view, name='despesa-atualiza-view'),
    path('eliminar/<int:my_id>/', despesa_elimina_view, name='despesa-elimina-view'),
]