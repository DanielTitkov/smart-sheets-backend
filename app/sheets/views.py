from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Sheet, Blueprint, Data, Rubric
from .serializers import SheetSerializer, BlueprintSerializer, DataSerializer, RubricSerializer


class BlueprintView(viewsets.ModelViewSet):
    queryset = Blueprint.objects.filter(published=True).all()
    serializer_class = BlueprintSerializer



class RubricView(viewsets.ModelViewSet):
    serializer_class = RubricSerializer

    def get_queryset(self):
        # by default get root rubrics (with no parent)
        queryset = Rubric.objects.filter(published=True, parent=None).all()

        parent_id = self.request.query_params.get('parent', None)
        if parent_id is not None: # if parent is specified get it's children
            queryset = Rubric.objects.filter(published=True, parent_id=parent_id).all()

        return queryset



class DataView(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer



class SheetView(viewsets.ModelViewSet):
    serializer_class = SheetSerializer

    def get_queryset(self):
        user = self.request.user
        return Sheet.objects.filter(deleted=False, user=user).order_by("-updated").all()