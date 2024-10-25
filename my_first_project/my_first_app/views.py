from django.shortcuts import render

# Create your views here.
def my_view(request):

    car_list = [
        {"title": "Audi"},
        {"title": "BMW"},
        {"title": "Mercedes"},
        {"title": "Toyota"},
        {"title": "Ford"},
        {"title": "Honda"},
        {"title": "Hyundai"},
        {"title": "Kia"},
        {"title": "Mazda"},
        {"title": "Nissan"},
    ]
    context = {
        "car_list": car_list
    }
    return render(request, "my_first_app/car_list.html", context)