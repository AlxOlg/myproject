from django.contrib import admin
from .models import Order, Product, User


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'quantity', 'date_product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'date_ordered']


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

