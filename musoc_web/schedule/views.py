from django.shortcuts import render
from .models import Reservation

# Create your views here.


def index(request):
    # Add variables in the custom_variables dict below to make them available within the rendered page
    title = "Welcome"
    custom_variables = {
        'title': title
    }
    return render(request, "schedule/home.html", custom_variables)

def calendar(request):
    # Add variables in the custom_variables dict below to make them available within the rendered page
    title = "Calendar"
    output = Reservation.objects.all()
    custom_variables = {
        'title': title,
        'output': output
    }
    return render(request, "schedule/calendar.html", custom_variables)