from django.urls import path, include
from .views import home, quienes_somos, registro, noticias, tiempo,login, recuperar, formulario
urlpatterns = [
    path('',home, name='home'),
    path('about_we/',quienes_somos, name='about_we'),
    path('noticias/',noticias, name='noticias'),
    path('tiempo/',tiempo, name='tiempo'),
    path('register/',registro, name='register'),
    path('login/',login, name='login'),
    path('recuperar/',recuperar, name='recuperar'),
    path('formulario/',formulario, name='formulario')
]