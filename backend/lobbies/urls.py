from django.urls import path
from . import views

urlpatterns = [
    path('', views.lobby_list_create_view),
    path('<int:pk>/join/', views ),
    path('<int:pk>/leave/', views ),
]