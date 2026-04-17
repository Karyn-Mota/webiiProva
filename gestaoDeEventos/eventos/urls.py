from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('novo/', views.formulario_eventos, name='formulario_eventos'),
]