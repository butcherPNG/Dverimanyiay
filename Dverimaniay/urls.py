from myapp import views
from myapp.views import *
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='index'),
    path('about', about_page, name='about'),
    path('catalog', catalog_page, name='catalog'),
    path('in', in_page, name='in'),
    path('map', map_page, name='map'),
    path('register', views.UserRegister.as_view(), name='register'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('account', account_page, name='account'),
    path("", include("contact.urls"))
]