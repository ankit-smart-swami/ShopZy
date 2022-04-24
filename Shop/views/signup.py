from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import make_password
from Shop.models.customer import Customer

class SignUp(View):
    @staticmethod
    def validateUser(customer):
        error_msg = ''
        if not customer.first_name:
            error_msg = "Please Enter First Name."
            
        elif len(customer.first_name) < 4 :
            error_msg = "First Name is too Shortcustomer.."
            
        elif not customer.last_name :
            error_msg = "Please Enter Last Name."
            
        elif len(customer.last_name) < 4 :
            error_msg = "Last Name is too Short."
        
        elif not customer.phone :
            error_msg = "Please Enter Mobile Number."
            
        # elif int(mobile) > 6000000000 and int(mobile) < 9999999999 :
            # error_msg = "Enter a valid is Mobile Number."
            
        elif not customer.password:
            error_msg = "Please Enter a password."
            
        elif len(customer.password) < 8 :
            error_msg = "Possword must be 8 character long." 
        
        elif customer.isExists() :
            error_msg = "Email is already registered."
            
        return error_msg
    
    def get(self, request):
        return render(request,'signup.html')
    
    def post(self, request):
        postData = request.POST
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        mobile = postData.get('mobile')
        email = postData.get('email')
        password = postData.get('password')
        value = {'first_name' : first_name, 'last_name' : last_name, 'mobile' : mobile,
                'email' : email}
        
        customer = Customer(first_name = first_name, last_name = last_name, phone = mobile,
                    email = email, password = password)
        
        error_msg = SignUp.validateUser(customer)
        if error_msg :
            data = {'err_msg' : error_msg, 'values' : value}
            return render(request, 'signup.html', data)
    
        customer.password = make_password(password)
        customer.register()
        return redirect('HomePage')
