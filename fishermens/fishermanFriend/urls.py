from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from apps.index import urls as index_urls
from apps.home import urls as home_urls
from apps.pescado import urls as pescado_urls
from apps.pescaria import urls as pescaria_urls
from apps.usuario import urls as usuarios_urls

urlpatterns = [
    path('', include(index_urls)),
    path('', include(home_urls)),
    path('usuario/', include(usuarios_urls)),
    path('pescaria/', include(pescaria_urls)),
    path('pescado/', include(pescado_urls)),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
