from django.urls import path
from . import views

#from django.conf.urls import include, url
#from django.views.generic import TemplateView


urlpatterns = [
    path('', views.index, name='index'),

]
