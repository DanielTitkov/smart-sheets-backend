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
    # data = DataSerializer(many=True, read_only=True)
    data = serializers.SerializerMethodField("get_data")

    class Meta:
        model = Sheet
        fields = ("id", "created", "updated", "blueprint", "data")
        depth = 1

    def get_data(self, obj):
        data = obj.data.all()
        # serializer = QuestionSerializer(questions, many=True)
        return { d.element_id : d.content for d in data }