from codecs import utf_16_be_decode
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import CreateUserForm
from . decorators import *
from accounts.models import *
from accounts.forms import *
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
    orders = request.user.customer.order_set.all()
    total_order = orders.count()
    order_deliver = orders.filter(status='Delivered').count()
    order_pending = orders.filter(status='Pending').count()
    context = {'total_order': total_order, 'order_deliver':order_deliver, 'order_pending': order_pending, 'orders':orders}
    return render(request, 'users/user.html', context)


@allowed_users(allowed_roles=['customer'])
def userSetting(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('user-account')
    context = {'form':form}
    return render(request, 'users/setting.html', context)