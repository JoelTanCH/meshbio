from django.urls import path

from . import views

urlpatterns = [
    #Enters root page, go to views.index page, look for name = index
    path('', views.base, name='test'), 
    path('joel/', views.joel, name='view joel'), 
    path('index/', views.index, name='index'), 
    path('test/', views.test, name='index'), 
]
