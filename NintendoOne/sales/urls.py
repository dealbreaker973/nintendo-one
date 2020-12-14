from django.urls import path
from sales import views

urlpatterns = [
    path('', views.GameListView.as_view(), name='game_list'),
]
