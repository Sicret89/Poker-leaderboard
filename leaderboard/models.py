# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from leaderboard.managers import PlayerManager
from django.db import models
from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver


class Prize(models.Model):
    total_prize = models.IntegerField(default=0, unique=True)

    def __str__(self):
        return str(self.total_prize)


class Player(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    E1 = models.IntegerField(default=0)
    E1B_AK = models.IntegerField(default=0)
    E1B_47 = models.IntegerField(default=0)
    E1_JOCKER = models.BooleanField(null=True, default=None)
    E2 = models.IntegerField(default=0)
    E2B_AK = models.IntegerField(default=0)
    E2B_47 = models.IntegerField(default=0)
    E2_JOCKER = models.BooleanField(null=True, default=None)
    E3 = models.IntegerField(default=0)
    E3B_AK = models.IntegerField(default=0)
    E3B_47 = models.IntegerField(default=0)
    E3_JOCKER = models.BooleanField(null=True, default=None)
    E4 = models.IntegerField(default=0)
    E4B_AK = models.IntegerField(default=0)
    E4B_47 = models.IntegerField(default=0)
    E4_JOCKER = models.BooleanField(null=True, default=None)
    E5 = models.IntegerField(default=0)
    E5B_AK = models.IntegerField(default=0)
    E5B_47 = models.IntegerField(default=0)
    E5_JOCKER = models.BooleanField(null=True, default=None)
    E6 = models.IntegerField(default=0)
    E6B_AK = models.IntegerField(default=0)
    E6B_47 = models.IntegerField(default=0)
    E6_JOCKER = models.BooleanField(null=True, default=None)
    E7 = models.IntegerField(default=0)
    E7B_AK = models.IntegerField(default=0)
    E7B_47 = models.IntegerField(default=0)
    E7_JOCKER = models.BooleanField(null=True, default=None)
    E8 = models.IntegerField(default=0)
    E8B_AK = models.IntegerField(default=0)
    E8B_47 = models.IntegerField(default=0)
    E8_JOCKER = models.BooleanField(null=True, default=None)
    E9 = models.IntegerField(default=0)
    E9B_AK = models.IntegerField(default=0)
    E9B_47 = models.IntegerField(default=0)
    E9_JOCKER = models.BooleanField(null=True, default=None)
    E10 = models.IntegerField(default=0)
    E10B_AK = models.IntegerField(default=0)
    E10B_47 = models.IntegerField(default=0)
    E10_JOCKER = models.BooleanField(null=True, default=None)
    E11 = models.IntegerField(default=0)
    E11B_AK = models.IntegerField(default=0)
    E11B_47 = models.IntegerField(default=0)
    E11_JOCKER = models.BooleanField(null=True, default=None)
    E12 = models.IntegerField(default=0)
    E12B_AK = models.IntegerField(default=0)
    E12B_47 = models.IntegerField(default=0)
    E12_JOCKER = models.BooleanField(null=True, default=None)
    _total = None

    objects = PlayerManager(
        total=F('E1') + F('E1B_AK') + F('E1B_47') + F('E2') + F('E2B_AK') + F('E2B_47') + F('E3') +
              F('E3B_AK') + F('E3B_47') + F('E4') + F('E4B_AK') + F('E4B_47') + F('E5') + F('E5B_AK') + F('E5B_47') +
              F('E6') + F('E6B_AK') + F('E6B_47') + F('E7') + F('E7B_AK') + F('E7B_47') + F('E8') + F('E8B_AK') +
              F('E8B_47') + F('E9') + F('E9B_AK') + F('E9B_47') + F('E10') + F('E10B_AK') + F('E10B_47') +
              F('E11') + F('E11B_AK') + F('E11B_47') + F('E12') + F('E12B_AK') + F('E12B_47'),
        total_jocker_e1=(F('E1') + F('E1B_AK') + F('E1B_47')) * 2 + F('E2') + F('E2B_AK') + F('E2B_47') + F('E3') +
                        F('E3B_AK') + F('E3B_47') + F('E4') + F('E4B_AK') + F('E4B_47') + F('E5') + F('E5B_AK') + F(
            'E5B_47') +
                        F('E6') + F('E6B_AK') + F('E6B_47') + F('E7') + F('E7B_AK') + F('E7B_47') + F('E8') + F(
            'E8B_AK') +
                        F('E8B_47') + F('E9') + F('E9B_AK') + F('E9B_47') + F('E10') + F('E10B_AK') + F('E10B_47') +
                        F('E11') + F('E11B_AK') + F('E11B_47') + F('E12') + F('E12B_AK') + F('E12B_47'),
        total_jocker_e2=F('E1') + F('E1B_AK') + F('E1B_47') + (F('E2') + F('E2B_AK') + F('E2B_47')) * 2 + F('E3') +
                        F('E3B_AK') + F('E3B_47') + F('E4') + F('E4B_AK') + F('E4B_47') + F('E5') + F('E5B_AK') + F(
            'E5B_47') +
                        F('E6') + F('E6B_AK') + F('E6B_47') + F('E7') + F('E7B_AK') + F('E7B_47') + F('E8') + F(
            'E8B_AK') +
                        F('E8B_47') + F('E9') + F('E9B_AK') + F('E9B_47') + F('E10') + F('E10B_AK') + F('E10B_47') +
                        F('E11') + F('E11B_AK') + F('E11B_47') + F('E12') + F('E12B_AK') + F('E12B_47'),
        total_e1=F('E1') + F('E1B_AK') + F('E1B_47'),
        total_e1_jocker=(F('E1') + F('E1B_AK') + F('E1B_47')) * 2,
        total_e2=F('E2') + F('E2B_AK') + F('E2B_47'),
        total_e2_jocker=(F('E2') + F('E2B_AK') + F('E2B_47')) * 2,
        total_e3=F('E3') + F('E3B_AK') + F('E3B_47'),
        total_e3_jocker=(F('E3') + F('E3B_AK') + F('E3B_47')) * 2,
        total_e4=F('E4') + F('E4B_AK') + F('E4B_47'),
        total_e4_jocker=(F('E4') + F('E4B_AK') + F('E4B_47')) * 2,
        total_e5=F('E5') + F('E5B_AK') + F('E5B_47'),
        total_e5_jocker=(F('E5') + F('E5B_AK') + F('E5B_47')) * 2,
        total_e6=F('E6') + F('E6B_AK') + F('E6B_47'),
        total_e6_jocker=(F('E6') + F('E6B_AK') + F('E6B_47')) * 2,
        total_e7=F('E7') + F('E7B_AK') + F('E7B_47'),
        total_e7_jocker=(F('E7') + F('E7B_AK') + F('E7B_47')) * 2,
        total_e8=F('E8') + F('E8B_AK') + F('E8B_47'),
        total_e8_jocker=(F('E8') + F('E8B_AK') + F('E8B_47')) * 2,
        total_e9=F('E9') + F('E9B_AK') + F('E9B_47'),
        total_e9_jocker=(F('E9') + F('E9B_AK') + F('E9B_47')) * 2,
        total_e10=F('E10') + F('E10B_AK') + F('E10B_47'),
        total_e10_jocker=(F('E10') + F('E10B_AK') + F('E10B_47')) * 2,
        total_e11=F('E11') + F('E11B_AK') + F('E11B_47'),
        total_e11_jocker=(F('E11') + F('E11B_AK') + F('E11B_47')) * 2,
        total_e12=F('E12') + F('E12B_AK') + F('E12B_47'),
        total_e12_jocker=(F('E12') + F('E12B_AK') + F('E12B_47')) * 2,
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
