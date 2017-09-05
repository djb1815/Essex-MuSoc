from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()


class ProfileNameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }


class ProfileDetailForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('band_name', 'fav_color')
        labels = {
            'band_name': 'Band/Booking Name',
            'fav_color': 'Booking Color'
        }
