from django.shortcuts import render, redirect
from ..log_app.models import User
from django.core.urlresolvers import reverse
from ..fridge_app.models import Fridge, Food

# Create your views here.
def index(request):
	user_object = User.userManager.get(id=request.session['id'])
	context = {
		'food' : Fridge.objects.filter(user_id=user_object)
	}
	return render(request, "fridge_templates/index.html", context)

def clear(request):
	return redirect(reverse('main'))

def addfood(request):
	user_object = User.userManager.get(id=request.session['id'])
	Food.objects.create(name=request.POST['name'])
	food = Food.objects.latest('created_at')
	Fridge.objects.create(user_id=user_object, food_id=food)
	context = {
		'food' : Fridge.objects.filter(user_id=user_object)
	}

	return render(request, "fridge_templates/index.html", context)
def remove(request, id):
	Fridge.objects.get(id=id).delete()
	return redirect(reverse('main'))

def append(request, id):
	user_object = User.userManager.get(id=request.session['id'])
	print id
	save = Food.objects.filter(id=id)
	context = {
		'food' : Fridge.objects.filter(user_id=user_object),
		'save' : save
	}
	print save
	return render(request, "fridge_templates/index.html", context)