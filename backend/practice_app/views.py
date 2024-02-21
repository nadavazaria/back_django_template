from django.shortcuts import render
from django.contrib.auth.models import User
from icecream import ic
from .models import Product
from rest_framework.response import Response as res
from rest_framework.decorators import api_view, permission_classes
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)


        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['admin'] = user.is_superuser

        # ...


        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



class ProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


@api_view(['GET'])
def index(req):
    return res({"message":"hello ass hole welcome"})


@api_view(['GET'])
def get_prods(req):
    prods = ProdSerializer(Product.objects.all(),many=True)
    return res(prods.data)



@api_view(["POST"])
def add_prod(req):
    new_prod = ProdSerializer(data = req.data)
    if new_prod.is_valid():
        new_prod.save()

    return res({'message':'product added successfully'})


@api_view(["PUT",'PATCH'])
def update_prod(req,id):
    prod_to_upd = Product.objects.get(id=id)
    new_prod_info = ProdSerializer(prod_to_upd,req.data)
    if new_prod_info.is_valid():
        new_prod_info.save()
    return res(new_prod_info.data)

@api_view(["DELETE"])
def delete_prod(req,id):
    prod_to_del = Product.objects.get(id=id)
    if prod_to_del:
        prod_to_del.delete()
        return res({"message":'product deleted successfuly',"deleted_product":ProdSerializer(prod_to_del).data})
    return res({"message":'product not found'})


@api_view(['POST'])
def register(req):
       
        User.objects.create_user(
        username= req.data["username"],
        email=req.data["email"],
        password=req.data["password"])
        return res({"message":'user added successfully'})
