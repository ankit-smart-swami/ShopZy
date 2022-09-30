from django.shortcuts import redirect, render, HttpResponse
from Shop.models import *
from django.views import View

class Auth(View):
    
    def get(self, request):
        key = request.GET.get('key')
        uname = request.GET.get('uname')
        print(key,uname)
        msg = ""
        user = User.get_customer_by_email(uname)
        if(user):
            if not(user.visited):
                if user.key == key:
                    msg = "Successfully Varified."
                    user.setVisited()
                    name = Customer.get_customer_by_email(user.email)
                    name.setVerified()
                else:
                    msg = "Invalid Link."
            else :
                msg = "Link Expired."
                
        else:
            msg = "User not Found."
            
        return HttpResponse(f"{msg}")
        