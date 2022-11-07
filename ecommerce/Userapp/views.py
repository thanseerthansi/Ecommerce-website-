
from django.contrib.auth.hashers import make_password
from ecommerce.globalimport import *
from Userapp.serializers import *
from Userapp.models import *

# Create your views here.

class UserView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        try:
            # print("data",self.request.data)
            userid = self.request.user.id
            qs = UserModel.objects.all()
            user = self.request.GET.get('user')
            # customer = self.request.GET.get('customer')
            admin = self.request.GET.get('admin')
            if user: qs = qs.filter(id=userid)
            # if customer: qs = qs. filter(is_customer = True)
            if admin: qs = qs. filter(is_admin = True)
            return qs
        except:return None
    def post(self,request):
        userobj = ""
        try: id = self.request.data['id']
        except:id=''
        try: username = self.request.data['username']
        except:username=''
       
        # try: email = self.request.data['email']
        # except:email=''
        try: password = self.request.data['password']
        except:password=''
       
        try:
            mandatory = ['username','password']
            data = Validate(self.request.data,mandatory)
            # print("okok")
            if id:
                # if id.isdigit():
                try:
                    # print("datapost",self.request.data)
                    user = UserModel.objects.filter(id=id)
                    if user.count():
                        user = user.first()
                    else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"User not found"})
                    # if email != user.email:
                    #     email_listqs = list(UserModel.objects.all().values_list('email',flat=True)) 
                    #     if email in email_listqs:return Response({"Status":status.HTTP_208_ALREADY_REPORTED,"Message":"Email Already Exist"})
                    serializer = UserSerializer(user,data=request.data,partial= True)
                    serializer.is_valid(raise_exception=True)
                    if password:
                        msg = "user details and password updated successfully"
                        user_obj = serializer.save(password = make_password(password))
                    else: 
                        msg = "User details updated successfully"
                        user_obj = serializer.save()
                    
                    return Response({"Status":status.HTTP_200_OK,"Message":msg})
                except Exception as e:
                    # print(f"Exception occured{e}")
                    if  user_obj : user_obj.delete()
                    else : pass
                    return  Response({
                        "Status":status.HTTP_400_BAD_REQUEST,
                        "Message":f"Excepction occured {e}"
                    })
                # else: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":"Please provide valid user"})
            else:
                # print("id2",id)
                # mandatory = ['username','email']
                # data = Validate(self.request.data,mandatory)
                # if email:
                #     email_listqs = list(UserModel.objects.all().values_list('email',flat=True)) 
                #     if email in email_listqs:return Response({"Status":status.HTTP_208_ALREADY_REPORTED,"Message":"Email Already Exist"})
                if data == True:                
                    try:
                        serializer = UserSerializer(data=request.data, partial=True)
                        serializer.is_valid(raise_exception=True)
                        msg = "Created New User"
                        user_obj = serializer.save(password=make_password(self.request.data['password']))    
                        return Response({"Status":status.HTTP_200_OK,"Message":msg})
                    except Exception as e :
                        return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e),})
                else : return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":data})
        except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})
   
    def delete(self,request):
        try:
            id = self.request.data['id']
            obj = UserModel.objects.filter(id=id)
            if obj.count():
                obj.delete()
                return Response({"Status":status.HTTP_200_OK,"Message":"Successfully Deleted"})
            else:return Response({"Status":status.HTTP_404_NOT_FOUND,"Message":"No Records Found with given id"})
        except Exception as e:return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e)})

class WhoAmI(ListAPIView):
    
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        try:
            return Response({
                "Status":1,
                "Data":self.request.user.username   
            })
        except Exception as e: return Response({"Status":status.HTTP_400_BAD_REQUEST,"Message":str(e),})

        
