from django.db import models
from django.forms import ModelForm

from django.conf import settings
from colorful.fields import RGBColorField

# Create your models here.


class Reservation(models.Model):
    time_slot = models.DateTimeField('time slot scheduled')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reserved_for = models.CharField(max_length=120)
    creation_date = models.DateTimeField(auto_now_add=True)
    res_color = RGBColorField(default='#5DADE2')

    def __str__(self):
        return str(self.reserved_for)
