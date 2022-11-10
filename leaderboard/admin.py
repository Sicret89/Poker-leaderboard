# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.

from .models import League, SingleTournament, Tournament, Admin

admin.site.register(League)
admin.site.register(Admin)
admin.site.register(Tournament)
admin.site.register(SingleTournament)
