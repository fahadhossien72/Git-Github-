from multiprocessing import context
from django.shortcuts import render
from accounts.models import *
from accounts.forms import *
# Create your views here.
def home(request):
    orders = Order.objects.all()
    customer = Customer.objects.all()
    total_order = orders.count()
    total_customer = customer.count()
    order_deliver = orders.filter(status='Delivered').count()
    order_pending = orders.filter(status='Pending').count()
    context = {'total_order':total_order, 'total_customer':total_customer, 'order_deliver':order_deliver, 'order_pending':order_pending, 'customers':customer, 'orders':orders}
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'accounts/product.html', context)

def customers(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_order = orders.count()
    context = {'customer':customer, 'orders':orders, 'total_order':total_order}
    return render(request, 'accounts/customer.html', context)



def createOrder(request):
    form = OrderForm()
    if request.methoad == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request, 'accounts/create_form.html', context)