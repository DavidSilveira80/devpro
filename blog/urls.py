from tkinter.font import names

from django.urls import path
from . import views
urlpatterns = [
    path('portao', views.portao),
    path('sala', views.sala),
    path('quarto', views.quarto)
]