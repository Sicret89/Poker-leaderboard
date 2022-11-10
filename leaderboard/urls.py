from django.urls import include, path

from . import views
from .views import ProfileListView, TournamentListView, AddPleayer

urlpatterns = [
    path("profiles_list/", ProfileListView.as_view(), name="leaderboard_list"),
    path("single_tournament_list/", TournamentListView.as_view(), name="single_tournament_list"),
    path("add_player", AddPleayer.as_view(), name="add_player"),
]

