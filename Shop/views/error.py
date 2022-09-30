from django.shortcuts import redirect, render
from Shop.models import *
from django.views import View



class Error(View):
    def get(self,request):
        return render(request,"notFound.html")