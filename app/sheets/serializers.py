from rest_framework import serializers
from .models import Sheet, Blueprint, Data


class BlueprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blueprint
        fields = ("__all__")
        depth = 1



class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ("__all__")
        depth = 0


class SheetSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    data = DataSerializer(many=True, read_only=True)
    blueprint = BlueprintSerializer(many=False, read_only=True)

    class Meta:
        model = Sheet
        depth = 1
        fields = ("id", "user", "created", "updated", "blueprint", "data")
        extra_kwargs = {
            'blueprint': {'read_only': True},
        }