from django.urls import path

from .views import choose_rank
from .views import register_rankweight
from .views import register_rankamount
from .views import update_rankweight
from .views import update_rankamount
from .views import delete_rankweight
from .views import delete_rankamount


urlpatterns = [
    path('rankings/', choose_rank, name="rankings"),
    path('registo_rankweight/', register_rankweight, name="registro_rankweight"),
    path('registro_ranksize/', register_rankamount, name="registro_rankamount"),
    path('atualiza_rankweight/<int:id>/', update_rankweight, name="atualiza_rankweight"),
    path('atualiza_ranksize/<int:id>/', update_rankamount, name="atualiza_rankamount"),
    path('deleta_competidor_peso/<int:id>/', delete_rankweight, name="deleta_competidor_peso"),
    path('deleta_competir_quantidade/<int:id>/', delete_rankamount, name="deleta_competidor_quantidade"),
]