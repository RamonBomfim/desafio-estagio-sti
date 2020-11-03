from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView
from .forms import UserAdminCreationForm
from .models import User


class RegisterView(CreateView):
    form_class = UserAdminCreationForm
    template_name = 'usuario/registro.html'
    model = User
    success_url = reverse_lazy('login')


class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'usuario/atualiza_dados_usuario.html'
    fields = ['name', 'cpf', 'phone', 'address', 'complement', 'image']
    success_url = reverse_lazy('conta')

    def get_object(self):
        return self.request.user


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'usuario/confirmacao_delete_usuario.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user
