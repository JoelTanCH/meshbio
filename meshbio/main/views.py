from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("<h1> mesh bio </>")

def joel(response):
    return HttpResponse("<h1> JOEL </>")