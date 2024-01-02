from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import product
from .serializers import productserializer
class latestproductlist(APIView):
    def get(self , request , format=None):
        product=product.objects.all[0:4]
        serializer=productserializer(product, many=True)
        return Response(serializer.data)
