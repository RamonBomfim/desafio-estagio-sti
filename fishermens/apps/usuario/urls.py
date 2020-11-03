from django.urls import path

from apps.usuario.views import RegisterView, UpdateUserView, DeleteUserView, TemplateView


urlpatterns = [
    path('registro/', RegisterView.as_view(), name="registro"),
    path('conta/', TemplateView.as_view(
        template_name='usuario/conta_usuario.html'), name="conta"),
    path('conta/atualiza/dados/', UpdateUserView.as_view(), name="atualiza_dados_usuario"),
    path('conta/deleta/', DeleteUserView.as_view(), name="deletar_conta"),
]
