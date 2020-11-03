from django.urls import path
from apps.home.views import HomeTemplateView


urlpatterns = [
    path('home/', HomeTemplateView.as_view(), name='home'),
]