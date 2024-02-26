from django.contrib import admin
from django.urls import path
#from .views import *
from . import views
urlpatterns = [
    path('sign_up', views.sign_up, name='sign_up'),]