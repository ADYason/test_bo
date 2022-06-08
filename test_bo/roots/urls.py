from django.urls import path

from . import views

app_name = 'roots'

urlpatterns = [
    path('', views.RootsView.as_view(), name='list'),
    path('form/', views.roots_create, name='roots_form'),
]
