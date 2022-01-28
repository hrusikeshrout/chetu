"""employee_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from employee_app import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from employee_app.views import PostDetailView,PostCreateView,PostUpdateView,PostListView,PostDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('login', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('', PostListView.as_view(), name='blog-home'),
    path('home', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('api/', include('employee_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

