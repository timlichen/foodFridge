from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
	return render(request, "fridge_templates/index.html")


