from django.urls import path

from . import views

app_name = 'items'

urlpatterns = [
    path('', views.ItemsView.as_view(), name='list'),
    path('form/', views.items_create, name='items_form'),
]
