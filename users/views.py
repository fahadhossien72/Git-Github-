from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import CreateUserForm
# Create your views here.
def userLogin(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are successfully login')
            return redirect('dashboard')
        else:
             messages.error(request, 'You account was not created!')
    context = {}
    return render(request, 'users/login.html', context)

def userLogout(request):
    logout(request)
    messages.success(request, 'You are successfully logout')
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.info(request, 'Your registration successfully complete!')
            return redirect('login')
        else:
            messages.error(request, 'You account was not created!')
    context = {'form': form}
    return render(request, 'users/registration.html', context)