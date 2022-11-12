# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.urls import reverse


class League(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Tournament(models.Model):
    name = models.CharField(max_length=250, unique=True)
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return str(self.name)


class SingleTournament(models.Model):
    name = models.CharField(max_length=250, unique=False)
    season = models.ManyToManyField(Tournament, related_name='t_name')
    player = models.CharField(max_length=150, null=True, blank=False, unique=True)
    points = models.IntegerField(default=0)
    bonus_a = models.IntegerField(default=0)
    bonus_b = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    totalpoints = models.IntegerField(default=0)

    @property
    def total_points(self):
        return self.points + self.bonus_a + self.bonus_b

    def get_all_players(self):
        for name in self.season.all():
            return name

    def __str__(self):
        return f"{self.player}"

    def get_absolute_url(self) -> str:
        """
        Retrieves url to self
        :return: Url to self resource.
        """
        return reverse("add_player")

    def save(self, *args, **kwargs):
        sum_of_points = self.points + self.bonus_a + self.bonus_b
        self.totalpoints = int(sum_of_points)/100
        super(SingleTournament, self).save(*args, **kwargs)


# Note: this is really a "user", but since Django already provides a User
#       model we don't want to override it. Instead we want to create some
#       additional properties and link it to a user.
# automatically create/update profile when a User is created
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Admin.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.admin.save()
