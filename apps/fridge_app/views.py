from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
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
		# food_objects = Fridge.fridgeManager.fridge(request.POST['food_name'])
		food_objects = Fridge.objects.create(food_name=request.POST['food_name'])
	return redirect('/')
