# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView


from leaderboard.models import SingleTournament, Tournament
from .forms import ProfileAddForm


class SingleTournamentListView(ListView):
    """
    View responsible for listing and filterig Single Tournament objects.
    """
    model = SingleTournament
    template_name = "leaderboard/single_tournament_list.html"
    paginate_by = 15
    ordering = ['-totalpoints']


class TournamentListView(ListView):
    """
    View responsible for listing and filterig Tournament objects.
    """
    model = Tournament
    template_name = "leaderboard/leaderboard_list.html"
    paginate_by = 15


    def get_context_data(self, **kwargs):
        context = super(TournamentListView, self).get_context_data(**kwargs)
        context['only_unique'] = SingleTournament.objects.values('name').distinct()
        return context


class AddPlayerView(SuccessMessageMixin, CreateView):
    """
    View responsible for adding Player objects.
    """
    model = SingleTournament
    template_name = "leaderboard/add_player.html"
    success_message = "Your player has been Created!"
    form_class = ProfileAddForm
