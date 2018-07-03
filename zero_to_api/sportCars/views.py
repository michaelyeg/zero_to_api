from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-

from django.shortcuts import render

from rest_framework import viewsets, permissions

from sportCars.models import sportsCar
from sportCars.serializers import sportsCarSerializer


class sportsCarViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = sportsCar.objects.all()
    serializer_class = sportsCarSerializer

'''
class CatViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
'''
