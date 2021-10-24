from django.shortcuts import render
from django.http import  HttpResponse

def index (requtest):
    return HttpResponse( "Hello, pybo 환영")

# Create your views here.
