from django.urls import path, include
from .views import sample_response

urlpatterns = [
    path('users', sample_response)
]
