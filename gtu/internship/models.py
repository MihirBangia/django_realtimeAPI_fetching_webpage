from django.db import models
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50,default="")
class Product(models.Model):
    product_name= models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    quantity=models.IntegerField(default=0)
    description=models.CharField(max_length=300,default="")
