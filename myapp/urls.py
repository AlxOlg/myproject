from django.urls import path
from django.conf.urls.static import static

from myproject import settings

from .views import OrderCreate, ProductCreate, UserCreate, catalog, index, about, orders, success, users

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('success/', success, name='success'),
    path('users/', users, name='users'),
    path('catalog/', catalog, name='catalog'),
    path('orders/', orders, name='orders'),
    path('user_add/', UserCreate.as_view(), name='user_add'),
    path('prod_add/', ProductCreate.as_view(), name='prod_add'),
    path('order_add/', OrderCreate.as_view(), name='order_add'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
