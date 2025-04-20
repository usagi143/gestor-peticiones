from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from . import forms
from forms import Peticion

# Create your views here.
def index(request):
    form_template = loader.get_template("peticion_form.html")
    return HttpResponse(form_template.render())

def get_name(request):
    if request.method == "POST":
        peticiones_form  = Peticion(request.POST)
        if peticiones_form.is_valid():
            return HttpResponseRedirect("")
    else:
        peticiones_form = Peticion()

    return render(request, "index.html", {"form": peticiones_form})


