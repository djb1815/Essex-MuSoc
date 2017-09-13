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
    day =  MuSocDiary.today
    dayNames = MuSocDiary.dayNameIter()
    daysInWeek = MuSocDiary.daysInWeek()
    daysInWeek2 = MuSocDiary.daysInWeek2()
    bookingHours = MuSocDiary.bookingHours

    custom_variables = {
        'title': title,
        'output': output,
        'year': year,
        'month': month,
        'day': day,
        'dayNames': dayNames,
        'daysInWeek': daysInWeek,
        'daysInWeek2': daysInWeek2,
        'bookingHours': bookingHours
    }
    return render(request, "schedule/calendar.html", custom_variables)