from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    #redireccion
    path('',views.index, name='index'),
    path('registro/',views.registro, name="registro"),
    path('perfil/',views.perfil, name="perfil"),
    path('administrador/',views.administrador, name="administrador"),

    #Metodos
    path('registro/crear_c',views.crear_cliente, name="crear_c"),
    path('perfil/crear_s', views.crear_solicitud, name="crear_s"),
]