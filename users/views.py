from codecs import utf_16_be_decode
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import CreateUserForm
from . decorators import *
# Create your views here.
@unauthenticated_user
def userLogin(request):
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are successfully login')
            return redirect('dashboard')
        else:
             messages.error(request, 'You username Or password Wrong!')
    context = {}
    return render(request, 'users/login.html', context)

def userLogout(request):
    logout(request)
    messages.success(request, 'You are successfully logout')
    return redirect('login')

@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            user = form.cleaned_data.get('username')
            messages.info(request, 'Account was created for'  + user)
            return redirect('login')
        else:
            messages.error(request, 'You account was not created!')
    context = {'form': form}
    return render(request, 'users/registration.html', context)

@allowed_users(allowed_roles=['customer'])
def userAccount(request):
    context = {}
    return render(request, 'users/user.html', context)