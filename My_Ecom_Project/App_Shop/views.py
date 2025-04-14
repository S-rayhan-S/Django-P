from django.shortcuts import render

# import class based views
from django.views.generic import ListView,DetailView

#Import models
from App_Shop.models import Product

# Create your views here.
class Home(ListView):
    model=Product
    template_name='App_Shop/home.html'
















