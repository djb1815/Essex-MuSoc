from django import forms
from colorful.forms import RGBColorField


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()


class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")
    band_name = forms.CharField(max_length=120, label="Band/Booking Name", required=False)
    fav_color = RGBColorField(label="Booking Color", required=False,
                              help_text="Choose a default color for reserved timeslots.")

    def save_profile(self, request, user):
        if self.has_changed():
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.profile.band_name = self.cleaned_data['band_name']
            user.profile.fav_color = self.cleaned_data['fav_color']
            user.save()
            user.profile.save()
