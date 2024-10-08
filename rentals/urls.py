from django.urls import path
from . import views

urlpatterns = [
    path('', views.rental_list, name='rental_list'),
    path('rental/<int:pk>/', views.rental_detail, name='rental_detail'),
    path('rental/create/', views.rental_create, name='rental_create'),
    path('rental/<int:pk>/edit/', views.rental_update, name='rental_update'),
    path('rental/<int:pk>/delete/', views.rental_delete, name='rental_delete')
]