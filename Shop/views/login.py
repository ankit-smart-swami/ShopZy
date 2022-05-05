from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from django.contrib.auth.hashers import check_password
from Shop.models.customer import Customer


class Login(View):
    returnUrl = None
    def get(self, request):
        Login.returnUrl = request.GET.get('returnUrl')
        return render(request, 'login.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        customer = Customer.get_customer_by_email(email)
        err_msg = ''
        
        if customer :
            if check_password(password, customer.password):
                request.session['customerId'] = customer.id
                request.session['customerEmail'] = customer.email
                
                if Login.returnUrl:
                    return HttpResponseRedirect(Login.returnUrl)
                else :
                    Login.returnUrl = None
                    return redirect('HomePage')
            
            err_msg = 'Invalid Cridential'
            
        else :   
            err_msg = 'User not Found'
            
        data = data = {
                'err_msg' : err_msg,
                'email' : email
                }
        return render(request, 'login.html', data)


def logout(request):
    request.session.clear()
    return redirect('HomePage')