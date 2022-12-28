from django.urls import path

from . import views
from .views import (
    DashboardView,
    EventCreateView,
    EventDeleteView,
    EventUpdateView,
    EventView,
    Index,
    PrizeUpdateView,
    Season,
)

urlpatterns = [
    path("", Index.as_view(), name="leaderboard_list"),
    path("player/<int:pk>/", DashboardView.as_view(), name="dashboard"),
    path("prize/<int:pk>/", PrizeUpdateView.as_view(), name="total_prize"),
    path("E1/", Season.as_view(), name="episode1"),
    path("E2/", Season.as_view(), name="episode2"),
    path("E3/", Season.as_view(), name="episode3"),
    path("E4/", Season.as_view(), name="episode4"),
    path("E5/", Season.as_view(), name="episode5"),
    path("E6/", Season.as_view(), name="episode6"),
    path("E7/", Season.as_view(), name="episode7"),
    path("E8/", Season.as_view(), name="episode8"),
    path("E9/", Season.as_view(), name="episode9"),
    path("E10/", Season.as_view(), name="episode10"),
    path("E11/", Season.as_view(), name="episode11"),
    path("E12/", Season.as_view(), name="episode12"),
    path("events/", EventView.as_view(), name="events-list"),
    path("events/create/", EventCreateView.as_view(), name="event-create"),
    path("events/<int:pk>/", EventUpdateView.as_view(), name="event"),
    path(
        "events/<int:pk>/delete/",
        EventDeleteView.as_view(),
        name="event-delete",
    ),
]
