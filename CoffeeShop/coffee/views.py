from django.shortcuts import render
from django.http import HttpResponse
from .models import Coffee  # Assuming your model is named Coffee


def home(request):
    coffee = Coffee.objects.all()  # Use the model Coffee, not the local variable coffee
    return render(request, 'home.html', {'coffee': coffee})


