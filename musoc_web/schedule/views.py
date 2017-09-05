from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .forms import ProfileNameForm, ProfileDetailForm
from django.contrib import messages

# Create your views here.


def index(request):
    # Add variables in the custom_variables dict below to make them available within the rendered page
    title = "Welcome"
    custom_variables = {
        'title': title
    }
    return render(request, "schedule/home.html", custom_variables)


@login_required
@transaction.atomic
def profile(request):
    title = "Account Settings"
    if request.method == 'POST':
        name_form = ProfileNameForm(request.POST, instance=request.user)
        detail_form = ProfileDetailForm(request.POST, instance=request.user.profile)
        if name_form.is_valid() and detail_form.is_valid():
            name_form.save()
            detail_form.save()
            messages.success(request, 'Your profile has been successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        name_form = ProfileNameForm(instance=request.user)
        detail_form = ProfileDetailForm(instance=request.user.profile)
    custom_variables = {
        'title': title,
        'name_form': name_form,
        'detail_form': detail_form
    }
    return render(request, "account/profile.html", custom_variables)
