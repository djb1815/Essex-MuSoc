from django.shortcuts import render

# Create your views here.


def index(request):
    # Add variables in the custom_variables dict below to make them available within the rendered page
    title = "Welcome"
    custom_variables = {
        'title': title
    }
    return render(request, "schedule/home.html", custom_variables)
