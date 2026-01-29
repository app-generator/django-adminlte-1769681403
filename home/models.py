# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    member_since = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Boat_Types(models.Model):

    #__Boat_Types_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    py = models.IntegerField(null=True, blank=True)

    #__Boat_Types_FIELDS__END

    class Meta:
        verbose_name        = _("Boat_Types")
        verbose_name_plural = _("Boat_Types")



#__MODELS__END
