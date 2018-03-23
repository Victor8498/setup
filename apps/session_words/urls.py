from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index),  # This line has changed!
    url(r'^process$', views.process),
    url(r'^clear$', views.clear),
#  url(r'^create$', views.create),
#  url(r'^[0-9]$', views.show),     # This line has changed!
#  url(r'^[0-9]/edit$', views.edit),     # This line has changed!
#  url(r'^[0-9]/delete$', views.destroy)     # This line has changed!
]

#/{{number}}/delete