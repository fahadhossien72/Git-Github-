from multiprocessing import context
from django.shortcuts import redirect, render
from accounts.models import *
from accounts.forms import *
from django.forms import inlineformset_factory
from . filters import OrderFilter
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def home(request):
    orders = Order.objects.all()
    customer = Customer.objects.all()
    total_order = orders.count()
    total_customer = customer.count()
    order_deliver = orders.filter(status='Delivered').count()
    order_pending = orders.filter(status='Pending').count()
    context = {'total_order':total_order, 'total_customer':total_customer, 'order_deliver':order_deliver, 'order_pending':order_pending, 'customers':customer, 'orders':orders}
    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def products(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'accounts/product.html', context)

@login_required(login_url='login')
def customers(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    total_order = orders.count()
    context = {'customer':customer, 'orders':orders, 'total_order':total_order, 'myFilter':myFilter}
    return render(request, 'accounts/customer.html', context)


@login_required(login_url='login')
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=5)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none() ,instance=customer)
    # form = OrderForm(initial={'customer':customer})
    if request.method == "POST":
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context={'formset':formset, 'customer':customer}
    return render(request, 'accounts/create_form.html', context)

@login_required(login_url='login')
def updateOrder(request, pk):
    orders = Order.objects.get(id=pk)
    form = OrderForm(instance=orders)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=orders)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            pass
    context={'form':form}
    return render(request, 'accounts/create_form.html', context)

@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    else:
        pass
    context={'order':order}
    return render(request, 'accounts/delete_form.html', context)
