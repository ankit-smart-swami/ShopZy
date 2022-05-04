from django.shortcuts import redirect, render
from django.views import View
from Shop.models.order import Order
from Shop.models.category import Category


class Orders(View):
    def get(self, request):
        customerId = request.session.get("customerId")
        order = Order.get_order_by_customer(customerId)
        orders = {'orders' : order}
        
        return render(request, 'orders.html',orders)
    
    
    