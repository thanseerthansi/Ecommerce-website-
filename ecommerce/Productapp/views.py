
import json
from Productapp.serializers import *
from ecommerce.globalimport import *
import rest_framework

# Create your views here.
class CategoryView(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        try:
            category_type = self.request.GET.get('category_type')
            id = self.request.GET.get('id')
            qs = CategoryModel.objects.all()
            if category_type : qs = qs.filter(category_type=category_type)
            if id : qs = qs.filter(id=id)

            return qs
        except: return None
    
    def post(self,request):
        
        try:
            # print("data",self.request.data)
            try:id=self.request.data['id']
            except:id=''
            if id : 
                category_qs = CategoryModel.objects.filter(id=id)
                if category_qs.count():
                    category_qs = category_qs.first()
                    category_obj = CategorySerializer(category_qs,data=self.request.data,partial=True)
                    msg = "Updated Successfully"
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id"})
            else:
                category_obj = CategorySerializer(data=self.request.data,partial=True)
                msg="Saved Successfully"
            category_obj.is_valid(raise_exception=True)
            category_obj.save()
            return Response({"Status":status.HTTP_200_OK,"Message":msg})
        except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    
    def delete(self,request):
        try:
            id = self.request.data['id']
            obj = CategoryModel.objects.filter(id=id)
            if obj.count():
                obj.delete()
                return Response({"Status":status.HTTP_200_OK,"Message":"Successfully Deleted"})
            else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records Found with given id"})
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

class ImageView(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ImageSerializer
    
    def get_queryset(self):
        try:
         
            id = self.request.GET.get('id')
            qs = ImageModel.objects.all()    
            if id : qs = qs.filter(id=id)
            return qs
        except: return None
    
    def post(self,request):
        try:
            try:id=self.request.data['id']
            except:id=''
            if id : 
                image_qs = ImageModel.objects.filter(id=id)
                if image_qs.count():
                    image_qs = image_qs.first()
                    image_obj = ImageSerializer(image_qs,data=self.request.data,partial=True)
                    msg = "Updated Successfully"
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id"})
            else:
                image_obj = ImageSerializer(data=self.request.data,partial=True)
                msg="Saved Successfully"
            image_obj.is_valid(raise_exception=True)
            image_obj.save()
            return Response({"Status":status.HTTP_200_OK,"Message":msg})
        except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    
    def delete(self,request):
        try:
            id = self.request.data['id']
            obj = ImageModel.objects.filter(id=id)
            if obj.count():
                obj.delete()
                return Response({"Status":status.HTTP_200_OK,"Message":"Successfully Deleted"})
            else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records Found with given id"})
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})


class ProductView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        try:
         
            # print("status",self.request.GET.get('status'))
            statusp = self.request.GET.get('status')
            # print("ststy",statusp)
            Title = self.request.GET.get('Title')
            id = self.request.GET.get('id')
            category = self.request.GET.get('category')
            price = self.request.GET.get('price')
            qs = ProductModel.objects.all().select_related('category')
            if Title : qs = qs.filter(Title=Title)
            if statusp :qs=qs.filter(status=statusp)
            if category : qs = qs.filter(category__id = category)
            if id : qs = qs.filter(id=id)
            if price : qs = qs.filter(price=price)
            return qs.order_by('-id')
        except: return None
    
    def post(self,request):
        try:
            # print("data",self.request.data)
            try:id=self.request.data['id']
            except:id=''
            # print("id",id)
            try:category = self.request.data['category']
            except:category = ''
            # print("category",category)
            if category:
                category_qs = CategoryModel.objects.filter(id=category)
                if category_qs.count():
                    category_qs = category_qs.first()
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Category found with given id"})
            if id : 
                product_qs = ProductModel.objects.filter(id=id)
                if product_qs.count():
                    product_qs = product_qs.first()
                    if not category: category_qs=product_qs.category
                    product_obj = ProductSerializer(product_qs,data=self.request.data,partial=True)
                    msg = "Updated Successfully"
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id"})
            else:
                product_obj = ProductSerializer(data=self.request.data,partial=True)
                msg="Saved Successfully"
            product_obj.is_valid(raise_exception=True)
            product_saved = product_obj.save(category=category_qs)
            # for images post to image field and to  add in m2m image field
            # try:images = self.request.data['images']
            try:images = self.request.FILES.getlist('images')
            
            except:images=''
            # print("image",images)
            # dumpimage = json.dumps(images)
            # print("dumbimage",json.dumps(images))
            # loadimage=json.loads(dumpimage)
            # print("loadimage",loadimage)
            
            if images:
                # print("haveimage",images)
                # jsonimage = json.loads(self.request.data['images'])
        
                for image in images:
                    # print('imageiiiii',image)
                    image_obj = ImageSerializer(data={'image':image},partial=True)
                    # print("okrexception",image_obj)
                    image_obj.is_valid(raise_exception=True)
                    # print("okrexception",image_obj)
                    image_saved = image_obj.save()
                    product_saved.images.add(image_saved)
            
            return Response({"Status":status.HTTP_200_OK,"Message":msg})
        except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

    def patch(self,request):
        try:   
            # print(self.request.data)    
            id = self.request.data['id']
            # image = self.request.data['image']
            keyword = self.request.data['keyword']
            mandatory = ['keyword','id']
            data = Validate(self.request.data,mandatory)
            
            if data == True:
                product_qs = ProductModel.objects.filter(id=id)
                if product_qs.count():
                    product_qs = product_qs.first()
                    # print("edadu",self.request.data['images'])
                    image = json.loads(self.request.data['images'])
                    # ii=json.loads(image)
                    # print("sdfdgd",ii)
                    # print("iimage",image)
                    for i in image:
                        # print("iiifs",i)
                        if keyword == "add":
                            image_qs = ImageModel.objects.filter(id=i)
                            if image_qs.count():
                                product_qs.images.add(i)
                                msg = "image added successfully"                            
                            else :return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":i+"Not found"})
                        elif keyword =="remove" :
                            product_list =list( product_qs.images.all().values_list('id',flat=True))
                            # product_list = list(ProductModel.objects.filter(images=product).values_list('product',flat=True))
                            # print("productlist",product_list)
                            if i in product_list:
                                product_qs.images.remove(i)
                                msg = "image removed successfully"
                                # print("cool",i)
                                productwithimage = ProductModel.objects.filter(images=int(i))
                                # print("productwithimage",productwithimage)
                                if productwithimage.count():
                                    pass
                                   
                                else:
                                    img=ImageModel.objects.filter(id=i)
                                    if img.count():
                                        img.delete()


                            else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"image with id"+i+"Not Found"})
                    return Response({"Status":status.HTTP_200_OK,"Message":msg})
            else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":data})       
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    
    def delete(self,request):
        try:
            # print("sgdd",self.request.data)
            id = self.request.data['id']
            # print('id',id)
            obj = ProductModel.objects.filter(id=id)
            if obj.count():
                # print("obj",obj)
                obj.delete()
                return Response({"Status":status.HTTP_200_OK,"Message":"Successfully Deleted"})
            else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records Found with given id"})
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

class PurchaseStatusView(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PurchaseStatusSerializer
    
    def get_queryset(self):
        try:

            id = self.request.GET.get('id')
            qs = PurchaseStatusModel.objects.all()
            if id : qs = qs.filter(id=id)
            return qs
        except: return None
    
    def post(self,request):
        try:
            try:id=self.request.data['id']
            except:id=''
            if id : 
                purchase_status_qs = PurchaseStatusModel.objects.filter(id=id)
                if purchase_status_qs.count():
                    purchase_status_qs = purchase_status_qs.first()
                    purchase_status_obj = PurchaseStatusSerializer(purchase_status_qs,data=self.request.data,partial=True)
                    msg = "Updated Successfully"
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id"})
            else:
                purchase_status_obj = PurchaseStatusSerializer(data=self.request.data,partial=True)
                msg="Saved Successfully"
            purchase_status_obj.is_valid(raise_exception=True)
            purchase_status_obj.save()
            return Response({"Status":status.HTTP_200_OK,"Message":msg})
        except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    
    def delete(self,request):
        try:
            id = self.request.data['id']
            obj = PurchaseStatusModel.objects.filter(id=id)
            if obj.count():
                obj.delete()
                return Response({"Status":status.HTTP_200_OK,"Message":"Successfully Deleted"})
            else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records Found with given id"})
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    

class CityView(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = CitySerializer
    
    def get_queryset(self):
        try:

            id = self.request.GET.get('id')
            qs = CityModel.objects.all()
            if id : qs = qs.filter(id=id)
            return qs
        except: return None
    
    def post(self,request):
        try:
            try:id=self.request.data['id']
            except:id=''
            if id : 
                city_qs = CityModel.objects.filter(id=id)
                if city_qs.count():
                    city_qs = city_qs.first()
                    city_obj = CitySerializer(city_qs,data=self.request.data,partial=True)
                    msg = "Updated Successfully"
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id"})
            else:
                city_obj = CitySerializer(data=self.request.data,partial=True)
                msg="Saved Successfully"
            city_obj.is_valid(raise_exception=True)
            city_obj.save()
            return Response({"Status":status.HTTP_200_OK,"Message":msg})
        except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    
    def delete(self,request):
        try:
            id = self.request.data['id']
            obj = CityModel.objects.filter(id=id)
            if obj.count():
                obj.delete()
                return Response({"Status":status.HTTP_200_OK,"Message":"Successfully Deleted"})
            else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records Found with given id"})
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    
class OrderView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        try:

            id = self.request.GET.get('id')
            purchase_status = self.request.GET.get("status")
            product = self.request.GET.get('product')
            customer_name = self.request.GET.get('customer_name')
            qs = OrderModel.objects.all().select_related('status')
            if product : qs = qs.filter(product__id=product)
            if id : qs = qs.filter(id=id)
            if purchase_status:qs=qs.filter(status__id=purchase_status)
            if customer_name: qs=qs.filter(customer_name=customer_name)
            return qs.order_by('-id')
        except: return None
    
    def post(self,request):
        try:
            #pass status not id 
            print("data",self.request.data)
            # try:order_data = self.request.data[0]
            # except:order_data =""
            # if order_data:
            try:purchasetatus = self.request.data['purchasestatus']
            except:purchasetatus = ''
            try:productid = self.request.data['product']
            except:productid=''
            if productid:
                product_qs = ProductModel.objects.filter(id = productid)
                if product_qs.count():
                    product_qs = product_qs.first()
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No record found with given id"})
            if purchasetatus:
                # print("purchasetatus",purchasetatus)
                status_qs = PurchaseStatusModel.objects.filter(status__icontains=purchasetatus)
                if status_qs.count():
                    status_qs = status_qs.first()
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No record found with given id"})
            try:order_id = self.request.data['id']
            except:order_id = ""
            if order_id :
                # print("order_id",order_id)
                order_data_qs = OrderModel.objects.filter(id=order_id)
                if order_data_qs.count():
                    order_data_qs=order_data_qs.first()
                    if not purchasetatus:status_qs = order_data_qs.status
                    if not productid:product_qs=order_data_qs.product
                    order_data_obj = OrderSerializer(order_data_qs,data=self.request.data,partial=True)
                    msg="Updated Successfully"
                    
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id"})
            else:
                order_data_obj =  OrderSerializer(data=self.request.data,partial=True)
                msg = "Saved Successfully"
            print("prodct",product_qs)
            order_data_obj.is_valid(raise_exception=True)
            order_data_saved = order_data_obj.save(status=status_qs,product=product_qs)
            return Response({"Status":status.HTTP_200_OK,"Message":msg})
                    
        except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    
    def delete(self,request):
        try:
            id = self.request.data['id']
            obj = OrderModel.objects.filter(id=id)
            if obj.count():
                obj.delete()
                return Response({"Status":status.HTTP_200_OK,"Message":"Successfully Deleted"})
            else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records Found with given id"})
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

           
class ContactView(ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ContactSerializer
    
    def get_queryset(self):
        try:
            id = self.request.GET.get('id')
            qs = ContactModel.objects.all()
            if id : qs = qs.filter(id=id)
            return qs.order_by('-id')
        except: return None
    
    def post(self,request):
        try:
            try:id=self.request.data['id']
            except:id=''
            if id : 
                contact_qs = ContactModel.objects.filter(id=id)
                if contact_qs.count():
                    contact_qs = contact_qs.first()
                    contact_obj = ContactSerializer(contact_qs,data=self.request.data,partial=True)
                    msg = "Updated Successfully"
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id"})
            else:
                contact_obj = ContactSerializer(data=self.request.data,partial=True)
                msg="Saved Successfully"
            contact_obj.is_valid(raise_exception=True)
            contact_obj.save()
            return Response({"Status":status.HTTP_200_OK,"Message":msg})
        except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    
    def delete(self,request):
        try:
            id = self.request.data['id']
            obj = ContactModel.objects.filter(id=id)
            if obj.count():
                obj.delete()
                return Response({"Status":status.HTTP_200_OK,"Message":"Successfully Deleted"})
            else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records Found with given id"})
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    
class MissingOrderView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = MissingOrderSerializer
    
    def get_queryset(self):
        try:
            id = self.request.GET.get('id')
            qs = MissingorderModel.objects.all()
            if id : qs = qs.filter(id=id)
            return qs.order_by('-id')
        except: return None
    
    def post(self,request):
        try:
            # print("dat",self.request.data)
            # print("dat",self.request.data)
            try:productid = self.request.data['product']
            except:productid=''
            if productid:
                product_qs = ProductModel.objects.filter(id=productid)
                if product_qs.count():
                    product_qs = product_qs.first()
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Product found with given id "})
            try:order_id = self.request.data['id']
            except:order_id = "" 
            if order_id :
                order_data_qs = MissingorderModel.objects.filter(id=order_id)
                if order_data_qs.count():
                    order_data_qs=order_data_qs.first()               
                    order_data_obj = MissingOrderSerializer(order_data_qs,data=self.request.data,partial=True)  
                    msg ="Updated Successfully"
                    
                else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records found with given id"})
            else:
                order_data_obj =  MissingOrderSerializer(data=self.request.data,partial=True)
                msg = "Saved Successfully"
            order_data_obj.is_valid(raise_exception=True)
            order_data_saved = order_data_obj.save(product=product_qs)          
            return Response({"Status":status.HTTP_200_OK,"Message":msg})
        except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
    
    def delete(self,request):
        try:
            
            id = self.request.data['id']
            obj = MissingorderModel.objects.filter(id=id)
            if obj.count():
                obj.delete()
                return Response({"Status":status.HTTP_200_OK,"Message":"Successfully Deleted"})
            else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records Found with given id"})
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

        
#not used v
# class DiscountView(ListAPIView):
#     serializer_class = DiscountSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#     def get_queryset(self):
#         try:
#             id = self.request.GET.get('id')
#             product = self.request.GET.get('product')
#             qs = DiscountModel.objects.all().select_related('product')
#             if id: qs = qs.filter(id=id)
#             if product : qs=qs.filter(product__id=product)
#             return qs
#         except: return None
    
#     def post(self,request):
#         try:
#             try:id=self.request.data['id']
#             except:id=''
#             try:product = self.request.data['product']
#             except : product = ''
#             if product: 
#                 product_qs = ProductModel.objects.filter(id=product).select_related('product','status','city')
#                 if product_qs.count():
#                     product_qs = product_qs.first()
#             if id :
#                 discount_qs = DiscountModel.objects.filter(id=id).select_related('product')
#                 if discount_qs.count():
#                     discount_qs = discount_qs.first()
#                     if not product:product_qs = discount_qs.product
#                 else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No record found with given id "})
#                 discount_obj = DiscountSerializer(discount_qs,data=self.request.data,partial=True)
#                 msg="Successfully Updated"
#             else:
#                 discount_obj = DiscountSerializer(data=self.request.data,partial=True)
#                 msg = "Saved Successfully"
#                 product_qs.update(is_discount=True)
#             discount_obj.is_valid(raise_exception=True)
#             discount_obj.save(product=product_qs)
#             return Response({"Status":status.HTTP_200_OK,"Message":msg})
#         except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
#     def delete(self,request):
#         try:
#             id = self.request.data['id']
#             obj = DiscountModel.objects.filter(id=id).select_related('product')
#             product = obj[0].product
#             if obj.count:
#                 obj.delete()
#                 discount_list = list(DiscountModel.objects.filter(product=product).values_list('product',flat=True))
#                 if  discount_list.count()==0:
#                     product_obj = ProductModel.objects.filter(id=product.id).update(is_discount=False)
#                 return Response({"Status":status.HTTP_200_OK,"Message":"Successfully deleted"})
#             else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No record found with given id"})
#         except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

