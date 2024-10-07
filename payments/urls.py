from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_list, name='payments-list'),
    path('create/', views.payment_create, name='payments-create'),
    path('<int:pk>/', views.payment_detail, name='payments-detail'),
    path('<int:pk>/edit/', views.payment_update, name='payments-update'),
    path('<int:pk>/delete/', views.payment_delete, name='payments-delete'),
]