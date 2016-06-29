from __future__ import unicode_literals
from ..log_app.models import User
from django.db import models

# Create your models here.
class Fridge(models.Model):
	user_id = models.ForeignKey(User)
	food_name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)