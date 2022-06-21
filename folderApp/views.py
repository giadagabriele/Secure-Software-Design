from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from folderApp.models import ObjectOnDB
from folderApp.serializers import ObjectOnDBSerializer


class ObjectOnDBList(generics.ListCreateAPIView):
    queryset = ObjectOnDB.objects.all()
    serializer_class = ObjectOnDBSerializer


class ObjectOnDBDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ObjectOnDB.objects.all()
    serializer_class = ObjectOnDBSerializer
