from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
    dummy index
    """
    return HttpResponse("Bacon bacon...")