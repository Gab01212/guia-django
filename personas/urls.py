from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_personas, name='lista_personas'),
    path('perfil/', views.perfil_persona, name='perfil_persona'),
]