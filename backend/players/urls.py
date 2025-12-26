from django.urls import path
from . import views

urlpatterns = [
    path('/', views.get_all_players, name='get_all_players'),
    path('/<int:pk>/', views.player_detail_view, name='player_detail_view'),
    path('/register/', views.register_player),
    path('/me/add-rank/', views.add_player_rank),
]