from django.shortcuts import render
from django.http import HttpResponse


def sample_response(request):
    return HttpResponse("sample user response")