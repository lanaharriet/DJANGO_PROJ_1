from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Welcome to Home Page!")
def login_view(request):
    return render(request,'Website/login.html')