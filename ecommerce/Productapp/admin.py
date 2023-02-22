from django.contrib import admin

from Productapp.models import *

# Register your models here.
admin.site.register(CategoryModel)
admin.site.register(ImageModel)
admin.site.register(ProductModel)
admin.site.register(PurchaseStatusModel)
admin.site.register(CityModel)
admin.site.register(OrderModel)
# admin.site.register(productorderedModel)
admin.site.register(ContactModel)
admin.site.register(MissingorderModel)
# admin.site.register(MissingorderedproductModel)
# admin.site.register(DiscountModel)