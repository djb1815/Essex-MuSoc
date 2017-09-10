from .booking_mgmt import MuSocDiary

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
    day =  MuSocDiary.current_date_num
    daysInWeek = []
    for i in range(7):
        daysInWeek.append(day+i)

    daysInWeek2 = [daysInWeek[6]+1]
    for i in range(1,7):
        daysInWeek2.append(daysInWeek2[0]+i)

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