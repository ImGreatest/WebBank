from django.urls import path
from . import views

urlpatterns = [
    path('', views.create, name='home'),
    path('mortgage', views.mortgage, name='mortgage'),
    path('credit', views.credit, name='credit'),
    path('deposit', views.deposit, name='deposit')
]