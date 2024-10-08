from django.urls import path
from . import views

urlpatterns = [
    path('', views.tenant_list, name='tenant_list'),
    path('tenant/<int:pk>/', views.tenant_detail, name='tenant_detail'),
    path('tenant/create/', views.tenant_create, name='tenant_create'),
    path('tenant/<int:pk>/edit/', views.tenant_update, name='tenant_update'),
    path('tenant/<int:pk>/delete/', views.tenant_delete, name='tenant_delete')
]