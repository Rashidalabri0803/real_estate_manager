from django.urls import path
from . import views

urlpatterns = [
    path('', views.rental_list, name='rentals-list'),
    path('create/', views.rental_create, name='rentals-create'),
    path('<int:pk>/', views.rental_detail, name='rentals-detail'),
    path('<int:pk>/edit/', views.rental_update, name='rentals-update'),
    path('<int:pk>/delete/', views.rental_delete, name='rentals-delete'),
]