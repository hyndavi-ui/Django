from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import operator
def home(requests):
    return HttpResponse('This is home page')
def aboutme(requests):
    return HttpResponse('Im Hyndavi') 
