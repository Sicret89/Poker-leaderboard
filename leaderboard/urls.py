from django.urls import path

from .views import Index, DashboardView

urlpatterns = [
    path("leaderboard_list/", Index.as_view(), name="leaderboard_list"),
    path('player/<int:pk>/', DashboardView.as_view(), name='dashboard')
]