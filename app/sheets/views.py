from django.shortcuts import render
from rest_framework import viewsets
from .models import Sheet, Blueprint, Data
from .serializers import SheetSerializer, BlueprintSerializer, DataSerializer

class SheetView(viewsets.ModelViewSet):
    queryset = Sheet.objects.all()
    serializer_class = SheetSerializer



class BlueprintView(viewsets.ModelViewSet):
    queryset = Blueprint.objects.all()
    serializer_class = BlueprintSerializer



class DataView(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer