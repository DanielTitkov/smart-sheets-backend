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



class DataNestedSerializer(serializers.Serializer):
    data = serializers.DictField(
        child=serializers.CharField(
            allow_blank=True
        ), 
        allow_empty=True
    )

    def to_representation(self, instance): 
        return { d.element_id : d.content for d in instance.all() }



class SheetSerializer(serializers.ModelSerializer):
    # data = serializers.SerializerMethodField("get_data")
    data = DataNestedSerializer()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Sheet
        depth = 1
        fields = ("id", "user", "created", "updated", "blueprint", "data")
        extra_kwargs = {
            'blueprint': {'read_only': True},
        }

    def get_data(self, obj):
        data = obj.data.all()
        return { d.element_id : d.content for d in data }