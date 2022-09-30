from django.urls import path
from .views import *
from Shop.middleware import *

urlpatterns = [
    path('',  Index.as_view() , name = 'HomePage'),
    path('signup/', SignUp.as_view(), name = 'SignUp'),
    path('login/', Login.as_view() , name = 'Login'),
    path('logout/', logout , name = 'Logout'),
    path('cart/', Cart.as_view(), name = 'Cart'),
    path('checkout', auth_middleware(CheckOut.as_view()), name = 'CheckOut'),
    path('orders/', auth_middleware(Orders.as_view()), name = 'Orders'),
    path('auth/', Auth.as_view(), name = 'Authenticate'),
    path('payment/', Payment.as_view(), name = 'Payment'),
    path('*/', Error.as_view(),name="*")
    
]