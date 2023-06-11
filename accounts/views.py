from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import Group
from .forms import OrderForm, CreateUserForm, CustomerForm
from django.forms import inlineformset_factory
from .filters import OrderFilter
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
# Create your views here.

@login_required(login_url='login_page')
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status="Delivered").count()
    pendings = orders.filter(status="Pending").count()

    context = {
        "orders": orders,
        "customers": customers,
        "total_orders": total_orders,
        "total_customers": total_customers,
        "delivered": delivered,
        "pendings": pendings
    }
    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login_page')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html',{'products': products})

@login_required(login_url='login_page')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()
    my_filter = OrderFilter(request.GET, queryset=orders)
    order = my_filter.qs
    context = {"customer": customer, "orders": orders, "order_count": order_count,"myFilter": my_filter}
    return render(request, 'accounts/customer.html', context=context)

@login_required(login_url='login_page')
@allowed_users(allowed_roles=['admin'])
def create_order(request, pk):
    order_from_set = inlineformset_factory(Customer, Order, fields=('product', 'status'))
    customer = Customer.objects.get(id=pk)
    # form = OrderForm(initial={'customer': customer})
    form_set = order_from_set(queryset=Order.objects.none(),instance=customer)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {"forms": form_set}
    return render(request, 'accounts/order_form.html', context=context)

@login_required(login_url='login_page')
@allowed_users(allowed_roles=['admin'])
def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login_page')
@allowed_users(allowed_roles=['admin'])
def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect("/")
    context = {"item": order}
    return render(request, 'accounts/delete.html', context=context)

@unauthenticated_user
def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username= username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Username of password is incorrect!")
    context = dict()
    return render(request, 'accounts/login.html', context)


def register_page(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username",'')
            group = Group.objects.get(name="customer")
            user.groups.add(group)
            Customer.objects.create(user=user, name = user.username)
            messages.success(request, f"Account was created for {username}")
            return redirect('/login')
    context = dict(form=form)
    return render(request, 'accounts/register.html', context)

@login_required(login_url='login_page')
def logout_user(request):
    logout(request)
    return redirect("/login")

@login_required(login_url='login_page')
@allowed_users(allowed_roles=['customer'])
def user_page(request):
    context = dict()
    try:
        orders = request.user.customer.order_set.all()
        context["orders"] = orders
    except Exception:
        pass
    return render(request, 'accounts/user.html', context)

@login_required(login_url='login_page')
@allowed_users(allowed_roles=['customer'])
def accounts_settings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            
    context = dict(
        form = form
    )
    return render(request, 'accounts/account_settings.html', context=context)