from django.shortcuts import render
from rest_framework.views import APIview
from rest_framework.response import response
from .models import product
from .serializers import productserializer
class latestproductlist(APIview):
    def get(self , request , format=None):
        product=product.objects.all[0:4]
        serializer=productserializer(product, many=True)
        return response(serializer.data)
