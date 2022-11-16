from django.contrib.messages.views import SuccessMessageMixin

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
