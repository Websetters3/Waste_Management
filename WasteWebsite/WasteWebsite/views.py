from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Django CodeWithHarry Cheatsheet')

def contact(request):
    return render(request, 'contact.html') 
