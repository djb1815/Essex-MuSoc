from .booking_mgmt import MuSocDiary
import datetime
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
    year = MuSocDiary.current_year
    month = MuSocDiary.current_month
    day =  datetime.datetime.date(datetime.datetime.now())
    daysInWeek = []
    for i in range(7):
        dayNum = day + datetime.timedelta(days=i)
        daysInWeek.append(dayNum.day)

    daysInWeek2 = []
    for i in range(7,14):
        dayNum = day + datetime.timedelta(days=i)
        daysInWeek2.append(dayNum.day)

    custom_variables = {
        'title': title,
        'output': output,
        'year': year,
        'month': month,
        'day': day,
        'daysInWeek': daysInWeek,
        'daysInWeek2': daysInWeek2
    }
    return render(request, "schedule/calendar.html", custom_variables)