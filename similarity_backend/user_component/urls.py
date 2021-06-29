from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.LoginUser.as_view()),
    path('register', views.RegisterUser.as_view())
]
