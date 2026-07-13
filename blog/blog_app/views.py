from django.shortcuts import render
from django.http import HttpResponse

def first_view(request):
    return HttpResponse("The main page")
def second_view(request):
    return HttpResponse("About us")
