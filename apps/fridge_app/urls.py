from django.conf.urls import url
from . import views

urlpatterns = [
   
    url(r'^$', views.index),
  	url(r'^fridge$', views.fridge, name="user_fridge")
]
