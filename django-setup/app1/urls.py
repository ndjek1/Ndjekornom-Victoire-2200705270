from django.urls import path #type: ignore
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('moisture/', views.soil_moisture, name='soil_moisture'),
]