from dataclasses import fields
from rest_framework import serializers
from .models import *





class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['email','password']