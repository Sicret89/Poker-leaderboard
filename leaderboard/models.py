# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Case, F, IntegerField, When
from django.db.models.signals import post_save
from django.dispatch import receiver

from leaderboard.managers import PlayerManager


class Prize(models.Model):
    total_prize = models.IntegerField(default=0, unique=True)
    logo_image = models.ImageField(
        default="logo_akvs47-main.png", upload_to="logo_pics"
    )

    def __str__(self):
        return str(self.total_prize)


class Event(models.Model):
    name = models.CharField(max_length=256)
    event_date = models.DateTimeField(
        blank=True, null=True, help_text="Day of the event"
    )
    notes = models.TextField(help_text="Textual Notes", blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Player(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    jocker_image = models.ImageField(
        default="jocker.jpg", upload_to="jocker_pics"
    )
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
        total=F("E1")
        + F("E1B_AK")
        + F("E1B_47")
        + F("E2")
        + F("E2B_AK")
        + F("E2B_47")
        + F("E3")
        + F("E3B_AK")
        + F("E3B_47")
        + F("E4")
        + F("E4B_AK")
        + F("E4B_47")
        + F("E5")
        + F("E5B_AK")
        + F("E5B_47")
        + F("E6")
        + F("E6B_AK")
        + F("E6B_47")
        + F("E7")
        + F("E7B_AK")
        + F("E7B_47")
        + F("E8")
        + F("E8B_AK")
        + F("E8B_47")
        + F("E9")
        + F("E9B_AK")
        + F("E9B_47")
        + F("E10")
        + F("E10B_AK")
        + F("E10B_47")
        + F("E11")
        + F("E11B_AK")
        + F("E11B_47")
        + F("E12")
        + F("E12B_AK")
        + F("E12B_47")
        + Case(
            When(E1_JOCKER=True, then=(F("E1") + F("E1B_AK") + F("E1B_47"))),
            When(E2_JOCKER=True, then=(F("E2") + F("E2B_AK") + F("E2B_47"))),
            When(E3_JOCKER=True, then=(F("E3") + F("E3B_AK") + F("E3B_47"))),
            When(E4_JOCKER=True, then=(F("E4") + F("E4B_AK") + F("E4B_47"))),
            When(E5_JOCKER=True, then=(F("E5") + F("E5B_AK") + F("E5B_47"))),
            When(E6_JOCKER=True, then=(F("E6") + F("E6B_AK") + F("E6B_47"))),
            When(E7_JOCKER=True, then=(F("E7") + F("E7B_AK") + F("E7B_47"))),
            When(E8_JOCKER=True, then=(F("E8") + F("E8B_AK") + F("E8B_47"))),
            When(E9_JOCKER=True, then=(F("E9") + F("E9B_AK") + F("E9B_47"))),
            When(
                E10_JOCKER=True, then=(F("E10") + F("E10B_AK") + F("E10B_47"))
            ),
            When(
                E11_JOCKER=True, then=(F("E11") + F("E11B_AK") + F("E11B_47"))
            ),
            When(
                E12_JOCKER=True, then=(F("E12") + F("E12B_AK") + F("E12B_47"))
            ),
            default=0,
            output_field=IntegerField(),
        )
    )

    @property
    def total_e1(self):
        if self.E1_JOCKER:
            return (self.E1 + self.E1B_47 + self.E1B_AK) * 2
        return self.E1 + self.E1B_47 + self.E1B_AK

    @property
    def total_e2(self):
        if self.E2_JOCKER:
            return (self.E2 + self.E2B_47 + self.E2B_AK) * 2
        return self.E2 + self.E2B_47 + self.E2B_AK

    @property
    def total_e3(self):
        if self.E3_JOCKER:
            return (self.E3 + self.E3B_47 + self.E3B_AK) * 2
        return self.E3 + self.E3B_47 + self.E3B_AK

    @property
    def total_e4(self):
        if self.E4_JOCKER:
            return (self.E4 + self.E4B_47 + self.E4B_AK) * 2
        return self.E4 + self.E4B_47 + self.E4B_AK

    @property
    def total_e5(self):
        if self.E5_JOCKER:
            return (self.E5 + self.E5B_47 + self.E5B_AK) * 2
        return self.E5 + self.E5B_47 + self.E5B_AK

    @property
    def total_e6(self):
        if self.E6_JOCKER:
            return (self.E6 + self.E6B_47 + self.E6B_AK) * 2
        return self.E6 + self.E6B_47 + self.E6B_AK

    @property
    def total_e7(self):
        if self.E7_JOCKER:
            return (self.E7 + self.E7B_47 + self.E7B_AK) * 2
        return self.E7 + self.E7B_47 + self.E7B_AK

    @property
    def total_e8(self):
        if self.E8_JOCKER:
            return (self.E8 + self.E8B_47 + self.E8B_AK) * 2
        return self.E8 + self.E8B_47 + self.E8B_AK

    @property
    def total_e9(self):
        if self.E9_JOCKER:
            return (self.E9 + self.E9B_47 + self.E9B_AK) * 2
        return self.E9 + self.E9B_47 + self.E9B_AK

    @property
    def total_e10(self):
        if self.E10_JOCKER:
            return (self.E10 + self.E10B_47 + self.E10B_AK) * 2
        return self.E10 + self.E10B_47 + self.E10B_AK

    @property
    def total_e11(self):
        if self.E11_JOCKER:
            return (self.E11 + self.E11B_47 + self.E11B_AK) * 2
        return self.E11 + self.E11B_47 + self.E11B_AK

    @property
    def total_e12(self):
        if self.E12_JOCKER:
            return (self.E12 + self.E12B_47 + self.E12B_AK) * 2
        return self.E12 + self.E12B_47 + self.E12B_AK

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
