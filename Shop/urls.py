from django.urls import path
from .views import *

urlpatterns = [
    path('',  Index.as_view() , name = 'HomePage'),
    path('signup/', SignUp.as_view(), name = 'SignUp'),
    path('login/', Login.as_view() , name = 'Login'),
    path('logout/', logout , name = 'Logout'),
    path('cart/', Cart.as_view(), name = 'Cart')
]