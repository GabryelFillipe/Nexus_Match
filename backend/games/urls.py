from django.urls import path
from . import views

urlpatterns = [
    path('games/', views.get_all_games, name='get_all_games'),
    path('games/<int:pk>/', views.get_game_by_id, name='get_game_by_id')
]