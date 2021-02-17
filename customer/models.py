from django.db import models
from istore.models import products
import datetime


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
    
    @staticmethod
    def get_cart_product(product_pk,user):
        product=products.objects.get(pk=product_pk)
        new_cart_obj=cart.objects.get(user=user,product_name=product.name)
        return new_cart_obj,product


class Orders(models.Model):
    product = models.ForeignKey(products,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    user = models.CharField(max_length=256)
    date = models.DateTimeField(default=datetime.datetime.now())
    address = models.CharField(max_length=256)
    contact_no = models.IntegerField(max_length=10)
    price = models.IntegerField()

    def __str__(self):
        return self.user
    


            

