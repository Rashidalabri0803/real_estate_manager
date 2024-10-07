from django.urls import path
from . import views

urlpatterns = [
    path('', views.rental_list, name='rentals-list'),
]