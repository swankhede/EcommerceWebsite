from django.db import models
from django.contrib.auth.models import User
from istore.models import products


# Create your models here.
class cart(models.Model):
    product_name=models.CharField(max_length=256)
    user = models.CharField(max_length=256)
    quantity = models.IntegerField()
    price = models.IntegerField()
    product_id = models.ForeignKey(products,on_delete=models.CASCADE)
    def __str__(self):
        return self.product_name
    
    @staticmethod
    def check_cart(quantity,product_name):
        if quantity<=0:
            cart.objects.filter(product_name=product_name).delete()
            

