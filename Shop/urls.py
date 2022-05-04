from django.urls import path

from Shop.views.checkout import CheckOut
from .views import *

urlpatterns = [
    path('',  Index.as_view() , name = 'HomePage'),
    path('signup/', SignUp.as_view(), name = 'SignUp'),
    path('login/', Login.as_view() , name = 'Login'),
    path('logout/', logout , name = 'Logout'),
    path('cart/', Cart.as_view(), name = 'Cart'),
    path('checkout', CheckOut.as_view(), name = 'CheckOut'),
    path('orders/', Orders.as_view(), name = 'Orders')
]