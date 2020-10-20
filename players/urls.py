from django.urls import path
from .views import PlayerView


app_name = "players"


urlpatterns = [
    path('players/', PlayerView.as_view()),
]