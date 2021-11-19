from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name="Main"),
path('contact', views.contact, name="contact"),
path('signup', views.signup, name="signup"),
path('login', views.handleLogin, name="handleLogin"),
path('logout', views.handleLogout, name="handleLogout")
]