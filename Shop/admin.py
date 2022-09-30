from django.contrib import admin

from .models import * 

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']
    
class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','verified']
    
class AdminStatus(admin.ModelAdmin):
    list_display = ['status']

class AdminOrder(admin.ModelAdmin):
    list_display = ['product','customer','quantity','date']
    
class AdminUser(admin.ModelAdmin):
    list_display = ['email','key','visited']
    
# Register your models here.
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Status,AdminStatus)
admin.site.register(Order,AdminOrder)
admin.site.register(User,AdminUser)