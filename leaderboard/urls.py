from django.urls import path

from . import views
from .views import Index, DashboardView, Season

urlpatterns = [
    path("leaderboard_list/", Index.as_view(), name="leaderboard_list"),
    path('player/<int:pk>/', DashboardView.as_view(), name='dashboard'),
    path("season/", Season.as_view(), name="season"),
]