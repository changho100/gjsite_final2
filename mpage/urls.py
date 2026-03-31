from django.urls import path

from . import views

app_name = 'mpage'

urlpatterns = [
    path('', views.index),
]