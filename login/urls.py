from django.urls import path
from login import views

urlpatterns = [
    
    path('',views.index24),
    path('user_login',views.user_login),
    ]