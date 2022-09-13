from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def base(response):
    #t = loader.get_template('home.html')
    #return t.render(response)
    return render(response, "base.html", {})
    #meshbio\main\templates

def test(response):
    return HttpResponse("<h1> TEST </>")


def joel(response):
    return HttpResponse("<h1> JOEL </>")

def index(response):
    return HttpResponse("<h1> INDEX </>")
