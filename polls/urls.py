import django.contrib.auth.views
from django.urls import path
from . import views
#from django.contrib.auth.forms import

urlpatterns = [
    path('', views.create, name='home'),
    path('mortgage', views.mortgage, name='mortgage'),
    path('credit', views.credit, name='credit'),
    path('deposit', views.deposit, name='deposit'),
    path('profile/<str:user>', views.profileUserHome, name='profile')
]