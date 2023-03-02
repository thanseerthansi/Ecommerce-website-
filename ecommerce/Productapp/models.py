# import email
# from email.policy import default
# from tkinter import CASCADE
# from unicodedata import category
from email.policy import default
from django.db import models
# from django.forms import CharField, DateTimeField

# Create your models here.
class CategoryModel(models.Model):
    category_type = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class ImageModel(models.Model):
    image = models.ImageField(upload_to='Image',blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now = True)

class ProductModel(models.Model):
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    brand = models.CharField(max_length=100,blank=True,null=True)
    code = models.CharField(max_length=100,blank=True,null=True)
    price = models.FloatField(default=0.0)
    old_price = models.FloatField(default=0.0)
    size = models.CharField(max_length=100,null=True,blank=True)
    quantity = models.FloatField(default=0.0)
    quanity_text = models.CharField(max_length=100,blank=True,null=True)
    rank = models.IntegerField(blank=True,null=True)
    Fake_order_sold =  models.IntegerField(blank=True,null=True)
    images = models.ManyToManyField(ImageModel)
    google_category = models.CharField(max_length = 100,blank=True,null=True)
    title = models.CharField(max_length=200,blank=True,null=True)
    purchase_price = models.IntegerField(default=0)
    price_list = models.CharField(max_length=100,blank=True,null=True)
    colour = models.CharField(max_length=100,blank=True,null=True) 
    delivery_charge = models.FloatField(default=0.0)
    is_discount = models.BooleanField(default=False)
    description = models.TextField(blank=True,null=True)
    status = models.BooleanField(default=True)
    vat = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now=True)

class PurchaseStatusModel(models.Model):
    status = models.CharField(max_length=100,null=True,blank=True)
    color= models.CharField(max_length=100,default="white")
    description = models.TextField(blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class CityModel(models.Model):
    city_name = models.CharField(max_length = 100,null=True)
    description = models.TextField(blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class OrderModel(models.Model):
    product = models.ForeignKey(ProductModel,on_delete = models.DO_NOTHING ,null=True)
    customer_name = models.CharField(max_length = 100,blank=True,null=True)
    delivery_address = models.CharField(max_length= 200,blank=True,null=True)
    quantity = models.FloatField(blank=True,null=True)
    status = models.ForeignKey(PurchaseStatusModel,on_delete=models.DO_NOTHING)
    missorder_status = models.BooleanField(default=False)
    city = models.CharField(max_length=100,blank=True,null=True)
    contact = models.CharField(max_length=200,blank=True,null=True)
    total = models.FloatField(default=0.0)
    delivery_charge = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    description = models.TextField(blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now = True)

# class productorderedModel(models.Model):
#     order_id = models.ForeignKey(OrderModel,on_delete = models.CASCADE)
#     product = models.ForeignKey(ProductModel,on_delete=models.DO_NOTHING,null=True,blank=True)
#     quantity = models.FloatField(blank=True,null=True)
#     subtotal = models.FloatField(blank=True,null=True)
#     description = models.TextField(blank=True,null=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now = True) 

class ContactModel(models.Model):
    address = models.CharField(max_length=200,blank=True,null=True)
    facebook = models.CharField(max_length=200,blank=True,null=True)
    email = models.CharField(max_length=200,blank=True,null=True)
    instagram = models.CharField(max_length=200,blank=True,null=True)
    whatsapp = models.CharField(max_length = 200, blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class MissingorderModel(models.Model):
    customer_name = models.CharField(max_length=200,blank=True,null=True)
    product = models.ForeignKey(ProductModel,on_delete=models.DO_NOTHING,null=True)
    contact = models.CharField(max_length = 100,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    delivery_address = models.CharField(max_length= 200,blank=True,null=True)
    quantity = models.FloatField(blank=True,null=True)

    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now=True)

# class MissingorderedproductModel(models.Model):
#     missorder_id = models.ForeignKey(MissingorderModel,on_delete=models.CASCADE)
#     product = models.ForeignKey(ProductModel,on_delete=models.DO_NOTHING)
#     created_date = models.DateTimeField(auto_now_add = True)
#     updated_date = models.DateTimeField(auto_now=True)
#not used this discount model in this project
# class DiscountModel(models.Model):
#     product = models.ForeignKey(ProductModel,on_delete = models.CASCADE)
#     quantity = models.IntegerField(default=0)
#     price = models.FloatField(default=0.0)
#     description = models.TextField(blank=True,null=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now=True)
