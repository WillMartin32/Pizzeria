from django.urls import path
from . import views

app_name = 'pizzas'

urlpatterns = [     # Must be same as view.py
    path('', views.index, name='index'),
]