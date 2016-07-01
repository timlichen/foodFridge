from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index, name='main'),
	url(r'^addfood$', views.addfood, name="addfood"),
	url(r'^clear$', views.clear, name='clear'),
	url(r'^remove/(?P<id>\d+)$', views.remove, name='remove'),
	url(r'^append/(?P<id>\d+)$', views.append, name='append')
]