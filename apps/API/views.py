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
	# Here you are going are going to want to remove the key "food seach" from the session to clear out the search bar.

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
	search_bar_food = Food.objects.get(id=id)
	print search_bar_food.name

	# adding appended food to request.session, also checking to see if request.session has the "food seach array" and if not creating it and then adding to it.

	# currently this is capping out a length of 2, maybe there is something here you can improve on, or maybe try something else.

	try:
		print "appending"
		request.session['food_search'].append(search_bar_food.name)
	except:
		request.session['food_search'] = []
		request.session['food_search'].append(search_bar_food.name)

	context = {
		'food' : Fridge.objects.filter(user_id=user_object),
	}
	print request.session['food_search']
	return render(request, "fridge_templates/index.html", context)
