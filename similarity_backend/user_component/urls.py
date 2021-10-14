from django.urls import path, include
from user_component import views

urlpatterns = [
    path('login', views.LoginUser.as_view()),
    path('register', views.RegisterUser.as_view()),
    path('userhistory', views.UserHistoryAPI.as_view()),
    path('add_credit/<int:pk>/<int:amt>', views.UserAmount.as_view()),
    path('compare', views.ComparisonAPI.as_view()),
    path('user_saved_data', views.GetUserSavedDetail.as_view()),
    path('user_compare', views.UserCompare.as_view())
]
