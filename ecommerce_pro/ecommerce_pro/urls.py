"""e_commerce_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from ecommerce_app import views

urlpatterns = [     
    path('admin/', admin.site.urls),
    path('', views.Wellcome),
    path('home', views.home),
    path('register',views.register, name='register'),
    path('login', views.Signin, name='login'),
    path('logout', views.logout, name='logout'),
    path('change_password', views.change_password, name='change_password'),

]
