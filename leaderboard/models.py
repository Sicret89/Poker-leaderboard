# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from leaderboard.managers import PlayerManager
from django.db import models
from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver


class Player(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    S1E1 = models.IntegerField(default=0)
    S1E2 = models.IntegerField(default=0)
    S1E3 = models.IntegerField(default=0)
    S1E4 = models.IntegerField(default=0)
    S1E5 = models.IntegerField(default=0)
    S1E6 = models.IntegerField(default=0)
    S1E7 = models.IntegerField(default=0)
    S1E8 = models.IntegerField(default=0)
    S1E9 = models.IntegerField(default=0)
    S1E10 = models.IntegerField(default=0)
    S1E11 = models.IntegerField(default=0)
    S1E12 = models.IntegerField(default=0)
    _total = None

    objects = PlayerManager(
        total=F('S1E1') + F('S1E2') + F('S1E3') +
        F('S1E4') + F('S1E5') + F('S1E6') +
        F('S1E7') + F('S1E8') + F('S1E9') +
        F('S1E10') + F('S1E11') + F('S1E12'),
    )

    def __str__(self):
        return self.name
    #
    # class Meta:
    #     ordering = ['S1E1', 'S1E2', 'S1E3']


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
