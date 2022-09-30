from django.shortcuts import redirect, render
from django.views import View
from Shop.models.product import Product
from Shop.models.category import Category

class Index(View):
    def get(self, request):
        if not request.session.get("cart"):
            request.session["cart"] = {}
        data = {}
        products = Product.get_all_products()
        categories = Category.get_all_category()
        categoryId = request.GET.get('category')
        data['id'] = None
        searchTxt = request.GET.get('Search')
        #print(searchTxt)
        if searchTxt :
            products = Product.get_product_by_txt(searchTxt)
            print(len(products))
        
        
        if categoryId :
            products = Product.get_products_by_categoryId(categoryId)
            data['id'] = categories[int(categoryId)-1]
            
        data['category'] = categories
        data['products'] = products
        data['size'] = len(products)
        print("You are : " , request.session.get('customerEmail'))
        return render(request,'index.html',data)
    
    def post(self,request):
        
        productId = request.POST.get('productId')
        value = request.POST.get('qty')
        print(value)
        cart = request.session.get('cart')

        if cart:
            qty = cart.get(productId)
            if qty == 1 and int(value) == -1:
                cart.pop(productId)   
            elif qty  : 
                cart[productId] = qty + int(value)
            else:
                cart[productId] = 1
        else :
            cart = {}
            cart[productId] = 1
        
        request.session['cart'] = cart
        print(request.session['cart'])        
        
        
        
        return redirect('HomePage')
