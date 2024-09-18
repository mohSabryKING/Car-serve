
from django.urls import path, re_path
from django.contrib.auth import views as auth_model
from .views import *

app_name = ""

urlpatterns = [
      path('login',auth_model.LoginView.as_view(template_name="registration/login.html"),name='login'),
      path('logout',auth_model.LogoutView.as_view(template_name="registration/logout.html"),name='logout'),
      path('',Menu.as_view(),name='home'),
      ]

