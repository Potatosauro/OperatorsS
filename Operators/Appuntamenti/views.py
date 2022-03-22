from django.shortcuts import render
from django.views.generic.list import ListView
# Create your views here.
from .models import Operator

class Operator(ListView):
    model = Operator
    template_name = "operator.html"