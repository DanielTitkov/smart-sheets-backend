from rest_framework import serializers
from .models import Sheet, Blueprint, Data, Rubric



class BlueprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blueprint
        fields = ("__all__")
        depth = 1



class RubricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rubric
        fields = ("__all__")
        depth = 1



class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ("__all__")
        read_only_fields = ("sheet",)
        depth = 0



class SheetSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    data = DataSerializer(many=True)
    blueprint = BlueprintSerializer(many=False, read_only=True)
    blueprint_id = serializers.PrimaryKeyRelatedField(
        queryset=Blueprint.objects.all(), 
        write_only=True, 
        source='blueprint'
    )

    class Meta:
        model = Sheet
        depth = 1
        fields = ["id", "user", "created", "updated", "deleted", "blueprint", "blueprint_id", "data"]

    def create(self, validated_data):
        data_units = validated_data.pop('data')
        sheet = Sheet.objects.create(**validated_data)
        for data_unit in data_units:
            Data.objects.create(sheet=sheet, **data_unit)
        return sheet

    def update(self, instance, validated_data):
        data_units = validated_data.pop('data')
        instance=super().update(instance,validated_data)
        for data_unit in data_units: # this is very slow, maybe use bulk_update or something
            updated = Data.objects.filter(sheet=instance, element_id=data_unit.get("element_id")).update(**data_unit)
            if not updated:
                Data.objects.create(sheet=instance, **data_unit)
        return instance