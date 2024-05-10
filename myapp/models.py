from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(unique=True, max_length=50)
    address = models.CharField(max_length=100, default='', blank=True)
    password = models.CharField(max_length=20)
    date_user = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'фио: {self.name}, тел: {self.phone}'


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)
    date_product = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'товар: {self.title}, цена: {self.price}'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'заказчик: {self.customer}, дата заказа: {self.date_ordered}'

