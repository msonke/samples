from django.urls import path
from FirstApp import views

urlpatterns = [
    path('', views.index, name='index'),
]
