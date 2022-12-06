from django.urls import path

from . import views
from .views import Index, DashboardView, Season

urlpatterns = [
    path("leaderboard_list/", Index.as_view(), name="leaderboard_list"),
    path('player/<int:pk>/', DashboardView.as_view(), name='dashboard'),
    path("single_event_list1/", Season.as_view(), name="season1"),
    path("single_event_list2/", Season.as_view(), name="season2"),
    path("single_event_list3/", Season.as_view(), name="season3"),
    path("single_event_list4/", Season.as_view(), name="season4"),
    path("single_event_list5/", Season.as_view(), name="season5"),
    path("single_event_list6/", Season.as_view(), name="season6"),
    path("single_event_list7/", Season.as_view(), name="season7"),
    path("single_event_list8/", Season.as_view(), name="season8"),
    path("single_event_list9/", Season.as_view(), name="season9"),
    path("single_event_list10/", Season.as_view(), name="season10"),
    path("single_event_list11/", Season.as_view(), name="season11"),
    path("single_event_list12/", Season.as_view(), name="season12"),
]