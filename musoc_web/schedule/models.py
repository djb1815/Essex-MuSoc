from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from colorful.fields import RGBColorField

# Create your models here.


class Reservation(models.Model):
    time_slot = models.DateTimeField('time slot scheduled')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reserved_for = models.CharField(max_length=120)
    creation_date = models.DateTimeField(auto_now_add=True)
    res_color = RGBColorField(default='#5DADE2')

    def __str__(self):
        return self.time_slot


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE)
    band_name = models.CharField(max_length=120, blank=True, default='')
    fav_color = RGBColorField(blank=True, default='#5DADE2')

    def __str__(self):
        return self.user.email


# Function to automatically generate UserProfile db entry whenever a new user is created
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()
