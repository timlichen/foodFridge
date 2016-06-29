from django.shortcuts import render, redirect
from .models import Fridge
from ..log_app.models import User
# Create your views here.
def index(request):
	context = {
		'food_item' : Fridge.objects.all()
	}
	return render(request, "fridge_app/index.html", context)

def fridge(request):
	if request.method == 'POST':
		Fridge.objects.create(food_name=request.POST['food_name'])
	return redirect('/')	