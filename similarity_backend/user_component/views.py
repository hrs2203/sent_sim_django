from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import User, UserHistory
from .serializers import UserSerialzer, UserHistorySerialzer


def sample_response(request):
    allUsers = list(User.objects.all())
    allUserJson = UserSerialzer(allUsers, many=True)
    return JsonResponse(allUserJson)