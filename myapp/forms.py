from django import forms

from .models import Order, Product, User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ['customer', 'products']

