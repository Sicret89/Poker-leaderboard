from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

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
    paginate_by = 15
    ordering = ['-total']

    def get_context_data(self, **kwargs):
        context = super(Season, self).get_context_data(**kwargs)
        context['season1'] = Player.objects.filter().values('S1E1'),
        context['season2'] = Player.objects.filter().values('S1E2'),
        return context

# def season1(request):
#     context = {
#         'season1': Player.objects.filter().values('S1E1', 'S1E2')
#     }
#     return render(request, 'leaderboard/single_event_list.html', context)