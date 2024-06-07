from django.urls import path
from myapp import views

urlpatterns = [
    path("dishes/<str:dish>", views.menuitems),
]
