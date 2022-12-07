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
    E1 = models.IntegerField(default=0)
    E2 = models.IntegerField(default=0)
    E3 = models.IntegerField(default=0)
    E4 = models.IntegerField(default=0)
    E5 = models.IntegerField(default=0)
    E6 = models.IntegerField(default=0)
    E7 = models.IntegerField(default=0)
    E8 = models.IntegerField(default=0)
    E9 = models.IntegerField(default=0)
    E10 = models.IntegerField(default=0)
    E11 = models.IntegerField(default=0)
    E12 = models.IntegerField(default=0)
    _total = None

    objects = PlayerManager(
        total=F('E1') + F('E2') + F('E3') +
        F('E4') + F('E5') + F('E6') +
        F('E7') + F('E8') + F('E9') +
        F('E10') + F('E11') + F('E12'),
    )

    def __str__(self):
        return self.name


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
