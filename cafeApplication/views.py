from django.shortcuts import render
from django.http import HttpResponse

def sayhello(request):
    return HttpResponse("Hey there!")