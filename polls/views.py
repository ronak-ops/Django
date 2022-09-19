from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Welcome(Request):
    return HttpResponse("Welcome to the official election website")