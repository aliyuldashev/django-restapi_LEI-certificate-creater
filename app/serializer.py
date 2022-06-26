from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import LEI_user, Address,Billing_data,Parent_companies
from rest_framework.response import Response
from drf_writable_nested import WritableNestedModelSerializer




class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ['id']
        depth = 1


class Parent_companiesSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    address = AddressSerializer(many=True)
    class Meta:
        model = Parent_companies
        exclude = ['id']


class UserSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    parent_company = Parent_companiesSerializer(many=False,allow_null=True,)
    address = AddressSerializer(many=True,allow_null=True)
    class Meta:
        model = LEI_user
        fields = '__all__'


