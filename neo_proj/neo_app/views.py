from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    return render(request,'login.html')
    
def home(request):
    usrname = request.POST['username']
    paswrd = request.POST['password']
    user = authenticate(username=usrname, password=paswrd)
    if user is not None:
        #login(user)
        return render(request,'home.html')
    else:
        return HttpResponse('fail')
    
def welcome(request):
    return render(request,'home.html')

def signup_form(request):
    return render(request,'signup_form.html')

def register_successful(request):
    usrname = request.POST['username']
    paswrd = request.POST['password']
    u = user = User.objects.create_user(username=usrname,password=paswrd)
    u.save()
    return render(request,'home.html')
        