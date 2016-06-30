from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import User

# Create your views here.
def index(request):
	return render(request, "index.html")

def login(request):
	if request.method == "POST":
		user = User.userManager.login(request.POST['email'], request.POST['password'])
		context = {'login' : user[1]}
		if user[0]:
			request.session['id'] = user[1].id
			request.session['name'] = user[1].first_name + " " + user[1].last_name
			return redirect(reverse('main'))
		else:
			print "does not work"
			return render(request, 'index.html', context)
def register(request):
	if request.method == 'POST':
		user_tuple = User.userManager.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['confirm_password'])

		context = { "errors": user_tuple[1]}
		print context
		if user_tuple[0]:
			request.session['email'] = user_tuple[1].email
			request.session['name'] = user_tuple[1].first_name + " " + user_tuple[1].last_name
			print "true"
			return redirect(reverse('home'))
			
		else:
			print "false"
			return render(request, "index.html", context)