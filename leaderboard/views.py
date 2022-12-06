from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.shortcuts import render, redirect

from leaderboard.forms import PlayerUpdateForm
from leaderboard.models import Player
from django.views import generic
from django.urls import reverse_lazy


class Index(generic.ListView):
    model = Player
    template_name = 'leaderboard/leaderboard_list.html'
    paginate_by = 15
    ordering = ['-total']


class DashboardView(SuccessMessageMixin, generic.UpdateView):
    model = Player
    form_class = PlayerUpdateForm
    template_name = 'leaderboard/dashboard.html'
    success_url = reverse_lazy('leaderboard_list')
    success_message = "%(name)s was edited successfully."


class Season(generic.ListView):
    model = Player
    template_name = 'leaderboard/single_event_list.html'
    # paginate_by = 15
    # ordering = ['-S1E2']
    # queryset = Player.objects.order_by('-total')

    # def get_queryset(self):
    #     return Player.objects.filter(
    #         set_name=self.request.GET.get('q')
    #     )
    #
    # def dispatch(self, *args, **kwargs):
    #     try:
    #         return super().dispatch(*args, **kwargs)
    #     except Http404:
    #         return redirect('core:dashboard')