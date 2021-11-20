from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name="Main"),
path('contact', views.contact, name="contact"),
path('signup', views.signup, name="signup"),
path('login', views.handleLogin, name="handleLogin"),
path('logout', views.handleLogout, name="handleLogout"),
path('about',views.about, name="about"),
path('wet',views.wet, name="wet"),
path('ewaste',views.ewaste, name="ewaste"),
path('plastic',views.plastic, name="plastic"),
path('other',views.other, name="other"),
path('case',views.case, name="case"),
path('links',views.links, name="links")
]