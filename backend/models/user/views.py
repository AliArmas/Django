from django.shortcuts import render
from .models import User
from models.user.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView 
import json
from django.http import HttpResponse
#
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

