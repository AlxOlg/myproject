from django.shortcuts import render
from django.views.generic import CreateView

from .models import Order, Product, User
from .forms import OrderForm, ProductForm, UserForm


class UserCreate(CreateView):
    model = User
    form_class = UserForm
    template_name = 'myapp/user_add.html'
    success_url = '/success'


class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'myapp/prod_add.html'
    success_url = '/success'


class OrderCreate(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'myapp/order_add.html'
    success_url = '/success'


def users(request):
    users = User.objects.all()
    return render(request, 'myapp/users.html', {'users': users})


def catalog(request):
    products = Product.objects.all()
    return render(request, 'myapp/catalog.html', {'products': products})


def orders(request):
    orders = Order.objects.all()
    return render(request, 'myapp/orders.html', {'orders': orders})


def index(request):
    return render(request, 'myapp/index.html')
    
    
def about(request):
    return render(request, 'myapp/about.html')


def success(request):
    return render(request, 'myapp/success.html')

