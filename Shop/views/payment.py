from django.shortcuts import redirect, render
from Shop.models import *
from django.views import View

import razorpay

razorpay_id = "rzp_test_kBgaaq8f90t6YM"
razorpay_account_id = "Y8PdnQkTBvwebS8MWuD4auWQ"


class Payment(View):
    def post(self,request):
        amount = 1000
        print(amount)
        razorpay_client = razorpay.Client(auth=(razorpay_id, razorpay_account_id))
        
        order_currency = 'INR'

        callback_url = 'http://127.0.0.1:8000/orders/'
        print(callback_url)
        notes = {'order-type': "basic order from the website", 'key':'value'}
        razorpay_order = razorpay_client.order.create(dict(amount=amount*100, currency=order_currency, notes = notes, receipt="Order123", payment_capture='0'))
        print(razorpay_order['id'])
        razorpay_order_id = razorpay_order['id']
        
        return render(request, 'firstapp/payment/paymentsummaryrazorpay.html', {'order':order, 'order_id': razorpay_order['id'], 'orderId':'Order123', 'final_price':amount, 'razorpay_merchant_id':razorpay_id, 'callback_url':callback_url})
        
        


