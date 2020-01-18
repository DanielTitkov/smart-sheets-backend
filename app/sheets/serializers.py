from rest_framework import serializers
from .models import Sheet, Blueprint, Data



class SheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sheet
        fields = ("__all__")
        depth = 1


class BlueprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blueprint
        fields = ("__all__")
        depth = 1



class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ("__all__")
        depth = 1