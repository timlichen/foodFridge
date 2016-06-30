from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
from datetime import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
class UserManager(models.Manager):
	def login(self, email, password):
		try:
			user = self.get(email=email)
			if bcrypt.hashpw(password.encode('utf-8'), user.password.encode('utf-8')) == user.password:
				return(True, user)
		except:
			return(False,{"login": "login failed"})
		return(False,{"login": "login failed"})

	def register(self, first_name, last_name, email, password, confirm_password):
		errors={}
		if len(first_name) < 2:
			errors['first_name'] = "First Name is too short"
		if len(last_name) < 1:
			errors['last_name'] = "Last Name is too short"
		if len(password) < 8:
			errors['password'] = "Password is too short"
		if password != confirm_password:
			errors['confirm_password'] = "Passwords must match"
		try:
			user = self.get(email__iexact=email)
			errors['invalid'] = "Invalid registration"
		except:
			pass
		if not EMAIL_REGEX.match(email):
			errors['email'] = "Please enter a valid email"
		if errors:
			return(False, errors)
		password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
		self.create(first_name=first_name, last_name=last_name, password=password, email=email)
		return(True, self.get(email=email))
class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.EmailField() #does auto validation for us!
	password = models.CharField(max_length=255) #when using BCrypt, it hashes out a long password crypt
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	userManager = UserManager()