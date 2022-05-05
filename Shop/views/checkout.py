from django.shortcuts import redirect, render
from Shop.models import *
from django.views import View


class CheckOut(View):
    def get(self,request):
        return redirect("Cart")
    def post(self, request):
        address = request.POST.get("Address")
        phone = request.POST.get("Phone")
        print(address,phone)
        customer = request.session.get("customerId")
        cart = request.session.get("cart")
        print(address, phone)
        
        products = Product.get_products_by_id(list(cart.keys()))
        
        for product in products:
            order = Order(
                customer = Customer(id = customer),
                product = product,
                price = product.price,
                quantity = cart.get(str(product.id)),
                address = address,
                mobile = phone)
            
            order.placeOrder()
            
            
        request.session["cart"] = {}   
        
        
        return redirect("Orders")
