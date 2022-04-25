from django.shortcuts import redirect, render
from django.views import View
from Shop.models.product import Product
from Shop.models.category import Category


class Cart(View):
    def get(self,request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        return render(request,'cart.html',{'products' : products})
    
    def post(self, request):
        productId = request.POST.get('productId')
        value = request.POST.get('qty')
        # print(value)
        cart = request.session.get('cart')

        qty = cart.get(productId)
        if qty == 1 and int(value) == -1:
            cart.pop(productId)   
        elif qty  : 
            cart[productId] = qty + int(value)
        else:
            cart[productId] = 1
        
        request.session['cart'] = cart
        #print(request.session['cart'])        
        
        
        
        return redirect('Cart')




