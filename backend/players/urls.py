from django.urls import path
from . import views

urlpatterns = [
    path('players/', views.get_all_players, name='get_all_players'),
    path('players/<int:pk>/', views.get_player_by_id, name='get_player_by_id')
]