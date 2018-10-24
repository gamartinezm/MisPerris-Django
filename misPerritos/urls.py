from django.urls import path
from . import views


urlpatterns = [
    path('', views.rescatados_list, name='rescatados_list'),
]
