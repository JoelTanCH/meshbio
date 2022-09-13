from django.urls import path

from . import views

urlpatterns = [
    #Enters root page, go to views.index page, look for name = index
    path('', views.index, name='index'), 
    path('joel/', views.joel, name='view joel'), 
]
