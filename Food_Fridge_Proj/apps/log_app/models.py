from __future__ import unicode_literals
import bcrypt
import re
from django.db import models
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# Create your models here.

class UserManager (models.Manager):
# custom manager to easily allow us to call methods that are specific to this project (i.e. login and register)
	def login(self, email, password):
		user = self.filter(email__iexact= email) #allows you to use case insensitive comparision
		if user and bcrypt.hashpw(password.encode('utf-8'), user[0].password.encode('utf-8')) == user[0].password: # see line 37  #should be classified as a successful login event
			print "bcrypt checkingkjsndcjknsadjkndskj"
			return(True, user[0])
		return(False, {"login", "login failed"}) #failed login

	def register(self, first_name, last_name, email, password, confirm_password): #used to confirm validations
		# we want to verify all the info and make sure that person is not already registered ,_- all of which cause errors!
		print "register path successful"
		errors = {}
		if len(first_name) <2:
			errors['first_name'] = "FIRST name is too short"
		if len(last_name)< 2: 
			errors['last_name'] = "LAST name is too short"

		if not EMAIL_REGEX.match(email):
			errors['email'] = "Please enter a valid EMAIL"
		if len(password) <8:
			errors['password'] = "PASSWORD is too short"
		if password != confirm_password:
			errors['confirm_password'] = "Passwords must match!"


		user = self.filter(email__iexact= email)

		if user: 	#if user is valid or alread in system
			errors['invalid'] = "Invalid registration"

		if errors:
			return(False, errors)  #sends our dictionary back to our controller
		#otherwise, register the individual 

		password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())	

		print "password set"
		self.create(first_name=first_name, last_name=last_name, password=password, email=email)
		print "createdddddd"
		print self.filter(email=email)

		return(True, self.filter(email=email)[0])




class User(models.Model):
	#prebuilt with a manager called objects
	#managers allows us to do SQL queries (either using object.raw <-- normal sql query)
	# ORM shortcuts .get, .filter, .find
		#get return a list
		#filter returns

	#we can now make a table (just like an ERD diagram)
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.EmailField() #does auto validation for us!
	password = models.CharField(max_length=255) #when using BCrypt, it hashes out a long password crypt
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	# super set of objects (its got everything objects (User) has + login & register)
	userManager= UserManager()


