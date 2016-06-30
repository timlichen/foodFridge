from __future__ import unicode_literals
from ..log_app.models import User
from django.db import models

# Create your models here.
class FridgeManager(models.Manager):

	def clean_fridge(self, food_name):
		Fridge.objects.all().delete()

class Fridge(models.Model):
	user = models.ForeignKey(User)
	food_name = models.CharField(max_length=100, blank=True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)