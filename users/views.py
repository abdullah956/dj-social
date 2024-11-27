from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User

def home(request):
    users = User.objects.all()  
    return render(request, 'home.html', {'users': users})

def logout_view(request):
    logout(request)
    return redirect('/')