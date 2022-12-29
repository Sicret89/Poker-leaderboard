import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

from leaderboard.forms import (
    EventCreateForm,
    EventUpdateForm,
    PlayerUpdateForm,
    PrizeUpdateForm,
)
from leaderboard.models import Event, Player, Prize


class Index(generic.ListView):
    template_name = "leaderboard/leaderboard_list.html"
    paginate_by = 15

    def get_queryset(self):
        return Player.objects.order_by("-total")

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context["prize_list"] = Prize.objects.all()
        return context


class DashboardView(SuccessMessageMixin, generic.UpdateView):
    model = Player
    form_class = PlayerUpdateForm
    template_name = "leaderboard/dashboard.html"
    success_url = reverse_lazy("leaderboard_list")
    success_message = "%(name)s was edited successfully."

    def get_queryset(self):
        return Player.objects.all()

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context["prize_list"] = Prize.objects.all()
        return context


class Season(generic.ListView):
    model = Player
    template_name = "leaderboard/single_event_list.html"

    def get_queryset(self):
        return Player.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Season, self).get_context_data(**kwargs)
        context["prize_list"] = Prize.objects.all()
        return context


class PrizeUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Prize
    form_class = PrizeUpdateForm
    template_name = "leaderboard/total_prize.html"
    success_url = reverse_lazy("leaderboard_list")
    success_message = "Pot was edited successfully."


class EventView(generic.ListView):
    model = Event
    template_name = "leaderboard/event_calendar.html"

    def get_queryset(self):
        now = datetime.date.today()
        self.queryset = Event.objects.filter(event_date__gte=now).order_by(
            "event_date"
        )
        return self.queryset

    def get_context_data(self, **kwargs):
        context = super(EventView, self).get_context_data(**kwargs)
        context["prize_list"] = Prize.objects.all()
        return context


class EventUpdateView(
    LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView
):
    model = Event
    form_class = EventUpdateForm
    template_name = "leaderboard/event_update.html"
    success_url = reverse_lazy("events-list")
    success_message = "%(name)s was edited successfully."

    def get_queryset(self):
        return Event.objects.all()

    def get_context_data(self, **kwargs):
        context = super(EventUpdateView, self).get_context_data(**kwargs)
        context["prize_list"] = Prize.objects.all()
        return context


class EventCreateView(
    LoginRequiredMixin, SuccessMessageMixin, generic.CreateView
):
    model = Event
    form_class = EventCreateForm
    template_name = "leaderboard/event_add.html"
    success_url = reverse_lazy("events-list")
    success_message = "Your event has been Created!"

    def get_context_data(self, **kwargs):
        context = super(EventCreateView, self).get_context_data(**kwargs)
        context["prize_list"] = Prize.objects.all()
        return context


class EventDeleteView(
    LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView
):
    model = Event
    template_name = "leaderboard/event_confirm_delete.html"
    success_url = reverse_lazy("events-list")
    success_message = "Your event has been Deleted!"
