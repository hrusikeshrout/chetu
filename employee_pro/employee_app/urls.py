from django.urls import path
from employee_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about,name='blog-about'),
]

