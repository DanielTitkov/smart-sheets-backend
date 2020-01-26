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
    class DataField(serializers.DictField):
        def to_representation(self, instance): 
            try:
                objects = instance.all()
            except:
                return {}
                return super().to_representation(instance)
            print(instance, type(instance))
            return { d.element_id : d.content for d in objects }

        def to_internal_value(self, data):
            return data

    data = DataField(
        child=serializers.CharField(
            allow_blank=True
        ), 
        allow_empty=True
    )





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