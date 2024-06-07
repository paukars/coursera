from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def menuitems(request, dish):
    items = {
        "pasta": "Pasta is a type of noodle",
        "falafel": "Falafel are deep fried petties",
        "cheesecake": "Cheesecake is a type of dessert",
    }

    description = items[dish]

    return HttpResponse(f"<h2> {dish} </h2>" + description)
