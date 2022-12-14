"""djangoWebbank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),
    path('mortgage/', include('polls.urls')),
    path('credit/', include('polls.urls')),
    path('deposit/', include('polls.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('profile/<str:user>', include('polls.urls')),
    path('profile/<str:user>/mortgage', include('polls.urls')),
    path('profile/<str:user>/credits', include('polls.urls')),
    path('profile/<str:user>/deposits', include('polls.urls')),
]
