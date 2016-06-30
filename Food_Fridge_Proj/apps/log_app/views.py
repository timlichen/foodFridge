from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
	return render(request, "index.html")

def login(request):
	#goes to model and try to login
	#model responds with either the user, or failure

	if request.method == 'POST':
		user_tuple = User.userManager.login(request.POST['emaillog'], request.POST['passwordlog'])
		if user_tuple[0]: #true or false from the returned tuple, if user is true
			request.session['email'] = user_tuple[1].email
			request.session['name'] = user_tuple[1].first_name + " " + user_tuple[1].last_name
			#return render a new page??
			return render(request, "success.html")

		else:
			print "Does not work"
			return redirect('/')

	#Do some stuff if user_tuple[0] is false redirect('/) and set error message. DO ON OWN



def register(request):
	if request.method == 'POST':
		print request.POST['first_name']
		user_tuple = User.userManager.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['confirm_password'])

		context = { "errors": user_tuple[1]}
		print context
		## make decisions based on user_tuple[0]
		if user_tuple[0]:
			print "true"
			return render(request, "success.html")
			
		else:
			print "gfalse"
			return render(request, "index.html", context)
			
	else:
		return redirect('/')
