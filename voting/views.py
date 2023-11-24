from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Candidates

# Create your views here.
def homepage(request):
    return render(request, 'voting/homepage.html')

def vote(request):
    candidates = Candidates.objects.all()
    return render(request, 'voting/vote.html', {'candidates': candidates})

def result(request):
    return render(request, 'voting/result.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        user.save()
        return redirect('signin')

    return render(request, 'voting/register.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('vote')
        else:
            return render(request, 'voting/signin.html')
    else:
        return render(request, 'voting/signin.html')
    

