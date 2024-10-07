from django.urls import path
from . import views

urlpatterns = [
    path('', views.property_list, name='property-list'),
    path('create/', views.property_create, name='property-create'),
    path('<int:pk>/edit/', views.property_update, name='property-update'),
    path('<int:pk>/delete/', views.property_delete, name='property-delete'),
    path('<int:pk>/', views.property_detail, name='property-detail'),
]