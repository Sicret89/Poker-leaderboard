from django.urls import path

from .views import SingleTournamentListView, TournamentListView, AddPlayerView

urlpatterns = [
    path("profiles_list/", SingleTournamentListView.as_view(), name="single_tournament_list"),
    path("single_tournament_list/", TournamentListView.as_view(), name="leaderboard_list"),
    path("add_player", AddPlayerView.as_view(), name="add_player"),
]
