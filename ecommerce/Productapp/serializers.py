# from dataclasses import fields
from rest_framework import serializers
from .models import *





class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    images=ImageSerializer(many=True)
    category = serializers.SerializerMethodField()
    class Meta:
        model = ProductModel
        fields = '__all__'
    def get_category(self,obj):
        if obj.category:
            v_obj = CategoryModel.objects.filter(id=obj.category.id)
            v_qs = CategorySerializer(v_obj, many=True)
            return v_qs.data
        else:pass
class PurchaseStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseStatusModel
        fields = '__all__'
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CityModel
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    
    status = serializers.SerializerMethodField()
   
    class Meta:
        model = OrderModel
        fields = '__all__'
    
    def get_status(self,obj):
        if obj.status:
            v_obj = PurchaseStatusModel.objects.filter(id=obj.status.id)
            v_qs = PurchaseStatusSerializer(v_obj,many=True)
            return v_qs.data
        else:pass
    def get_product(self,obj):
        if obj.product:
            v_obj = ProductModel.objects.filter(id=obj.product.id).select_related('category')
            v_qs = ProductSerializer(v_obj,many=True)
            return v_qs.data
        else:pass
# class Productorderedserializer(serializers.ModelSerializer):
#     product = serializers.SerializerMethodField()
#     order_id = serializers.SerializerMethodField()
#     class Meta:
#         model = productorderedModel
#         fields = '__all__'  
#     def get_product(self,obj):
#         if obj.product:
#             v_obj = ProductModel.objects.filter(id=obj.product.id).select_related('category')
#             v_qs = ProductSerializer(v_obj,many=True)
#             return v_qs.data
#         else:pass
#     def get_order_id(self,obj):
#         if obj.order_id:
#             # print("obj.order_id.id",obj.order_id.id)
#             v_obj = OrderModel.objects.filter(id=obj.order_id.id)
#             v_qs = OrderSerializer (v_obj,many=True)
#             return v_qs.data
#         else:pass

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = '__all__'

class MissingOrderSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    class Meta:
        model = MissingorderModel
        fields = '__all__'
    def get_product(self,obj):
        if obj.product:
            v_obj = ProductModel.objects.filter(id=obj.product.id).select_related('category')
            v_qs = ProductSerializer(v_obj,many=True)
            return v_qs.data
        else:pass
# class Missingorderedproductserializer(serializers.ModelSerializer):
#     product = serializers.SerializerMethodField()
#     missorder_id = serializers.SerializerMethodField()
#     class Meta:
#         model = MissingorderedproductModel
#         fields = '__all__'  
#     def get_product(self,obj):
#         if obj.product:
#             v_obj = ProductModel.objects.filter(id=obj.product.id).select_related('category')
#             v_qs = ProductSerializer(v_obj,many=True)
#             return v_qs.data
#         else:pass
#     def get_missorder_id(self,obj):        
#         if obj.missorder_id:
#             v_obj = MissingorderModel.objects.filter(id=obj.missorder_id.id)
#             v_qs = MissingOrderSerializer(v_obj,many=True)
#             return v_qs.data
#         else:pass    

# class DiscountSerializer(serializers.ModelSerializer):
#     product = serializers.SerializerMethodField()
#     class Meta:
#         model = DiscountModel
#         fields ='__all__' 
#     def get_product(self,obj):
#         if obj.product:
#             v_obj = ProductModel.objects.filter(id=obj.product.id).select_related('category')
#             v_qs = ProductSerializer(v_obj,many=True)
#             return v_qs.data
#         else:pass