import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

logger = logging.getLogger('django')


class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'home/home.html'
