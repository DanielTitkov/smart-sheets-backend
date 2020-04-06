from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Sheet, Blueprint, Data
from .serializers import SheetSerializer, BlueprintSerializer, DataSerializer


class BlueprintView(viewsets.ModelViewSet):
    queryset = Blueprint.objects.filter(published=True).all()
    serializer_class = BlueprintSerializer



class DataView(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer



class SheetView(viewsets.ModelViewSet):
    serializer_class = SheetSerializer

    def get_queryset(self):
        user = self.request.user
        return Sheet.objects.filter(deleted=False, user=user).order_by("-updated").all()