from django.db import models
from django import forms

# Create your models here.

class products(models.Model):
    name = models.CharField(max_length=256)
    price = models.IntegerField()
    description =  models.TextField()
    image = models.ImageField(upload_to='media',blank=True)
    category = models.CharField(max_length=256,blank=True)
    reviews = models.CharField(max_length=256,blank=True)
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_product_by_name(input_name):
        return products.objects.filter(name__contains=input_name)
    
    @staticmethod
    def get_product_by_category(category_name):
        if category_name:
            return products.objects.filter(category=category_name)
        else:
            return products.objects.all()

