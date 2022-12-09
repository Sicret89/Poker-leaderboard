from django.contrib.messages.views import SuccessMessageMixin

from leaderboard.forms import PlayerUpdateForm, PrizeUpdateForm
from leaderboard.models import Player, Prize
from django.views import generic
from django.urls import reverse_lazy


class Index(generic.ListView):
    template_name = 'leaderboard/leaderboard_list.html'
    paginate_by = 15
    ordering = ['-total']
    queryset = Player.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['prize_list'] = Prize.objects.all()
        context['player_list'] = self.queryset
        return context


class DashboardView(SuccessMessageMixin, generic.UpdateView):
    model = Player
    form_class = PlayerUpdateForm
    template_name = 'leaderboard/dashboard.html'
    success_url = reverse_lazy('leaderboard_list')
    success_message = "%(name)s was edited successfully."
    queryset = Player.objects.all()

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['prize_list'] = Prize.objects.all()
        context['player_list'] = self.queryset
        return context


class Season(generic.ListView):
    model = Player
    template_name = 'leaderboard/single_event_list.html'
    queryset = Player.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Season, self).get_context_data(**kwargs)
        context['prize_list'] = Prize.objects.all()
        context['player_list'] = self.queryset
        return context


class PrizeUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Prize
    form_class = PrizeUpdateForm
    template_name = 'leaderboard/total_prize.html'
    success_url = reverse_lazy('leaderboard_list')
    success_message = "Pot was edited successfully."
