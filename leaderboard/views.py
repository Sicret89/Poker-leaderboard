# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User, Group
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView, View

from .models import League, SingleTournament, Tournament, Admin
from .forms import ProfileAddForm
from django.urls import reverse
import csv


def index(request):
    return HttpResponse("Hello, world. You're at the API index.")


def leagues_list(request):
    leagues = League.objects.order_by('-id')
    output = serializers.serialize("json", leagues)
    return HttpResponse(output)
    # return HttpResponse("You're looking at all leagues.")


def leagues_get(request, league_id):
    return HttpResponse("You're looking at league %s." % league_id)


def leagues_users_list(request, league_id):
    return HttpResponse("You're looking at league %s, all users." % league_id)


def leagues_users_get(request, league_id, user_id):
    return HttpResponse("You're looking at league %s, user %s." % (league_id, user_id))


class ProfileListView(ListView):
    """
    View responsible for listing and filterig Profile objects.
    """
    model = SingleTournament
    template_name = "leaderboard/leaderboard_list.html"
    paginate_by = 15
    ordering = ['-points']
    # form_class = BookSearchForm


class TournamentListView(ListView):
    """
    View responsible for listing and filterig Profile objects.
    """
    model = Tournament
    template_name = "leaderboard/single_tournament_list.html"
    paginate_by = 15
    # ordering = ['-points']
    # form_class = BookSearchForm


class AddPleayer(SuccessMessageMixin, CreateView):
    """
    View responsible for adding Book objects.
    """
    model = SingleTournament
    template_name = "leaderboard/add_player.html"
    success_message = "Your pleayer has been Created!"
    form_class = ProfileAddForm


    # def get_success_url(self):
    #     return reverse('views:leaderboard_list')
        # return reverse('lawyer_detail', kwargs={'lawyer_slug': self.object.lawyer_slug})
