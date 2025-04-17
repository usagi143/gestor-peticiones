from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    variable = "hola desde santy"
    form_template = loader.get_template("peticion_form.html")
    form_context = {"variable": variable}
    return HttpResponse(form_template.render(form_context))