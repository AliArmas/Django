from django.shortcuts import render
from .models import Product
from models.product.serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView 
import json
from django.http import HttpResponse
#
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer