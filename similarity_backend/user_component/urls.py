from django.urls import path, include
from user_component import views

urlpatterns = [
    path('login', views.LoginUser.as_view()),
    path('register', views.RegisterUser.as_view()),
    path('userhistory', views.UserHistoryAPI.as_view()),
    path('comp', views.ComparisonAPI.as_view())
    
]
