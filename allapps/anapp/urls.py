from django.urls import path
from . import views


app_name = 'anapp'

urlpatterns = [
    path('', views.index, name='index'),
]
