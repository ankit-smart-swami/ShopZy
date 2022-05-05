from django.shortcuts import redirect

def auth_middleware(get_response):
    
    def middleware(request):
        returnUrl = request.META['PATH_INFO']
        
        if not request.session.get('customerId'):
            return redirect(f'/login?returnUrl={returnUrl}')
        
        response = get_response(request)
        
        return response
    
    return middleware