from django.db import models
from .category import Category

class Product(models.Model) :
    name = models.CharField(max_length = 25)
    price = models.IntegerField(default = 100)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    description = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'Uploads/images')
    
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    
    @staticmethod
    def get_products_by_id(product_ids):
        return Product.objects.filter(id__in = product_ids)
    
    @staticmethod
    def get_product_by_txt(txt):
        return Product.objects.filter(name__icontains = txt)
    
    @staticmethod
    def get_products_by_categoryId(category_id):
        if category_id :
            return Product.objects.filter(category = category_id)
        return Product.get_all_products()
    
    
    
    