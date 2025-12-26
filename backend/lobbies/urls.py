from django.urls import path
from . import views

urlpatterns = [
    path('', views.lobby_list_create_view),
    path('<int:pk>/join/', views.player_lobby_join ),
    path('<int:pk>/leave/', views.player_leave_lobby ),
]