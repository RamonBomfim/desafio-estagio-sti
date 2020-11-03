from django.urls import path

from .views import fishing_data
from .views import new_fishing
from .views import update_fishing
from .views import delete_fishing

urlpatterns = [
    path('fishing/', fishing_data, name="informacoes_pescaria"),
    path('new_fishing/', new_fishing, name="nova_pescaria"),
    path('update_fishing/<int:id>', update_fishing, name="atualiza_pescaria"),
    path('delete_fishing/<int:id>', delete_fishing, name="deleta_pescaria"),
]
