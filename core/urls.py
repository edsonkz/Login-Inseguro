from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name = "index"),
    path('mensagens', views.mensagens, name = "mensagens"),
    path('sair', views.sair, name = "sair")
]
