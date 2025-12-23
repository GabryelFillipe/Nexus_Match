from django.urls import path
from . import views

urlpatterns = [
    path('teste/', views.teste_api, name='teste_api'),
    path('ola/', views.ola, name='ola')
]