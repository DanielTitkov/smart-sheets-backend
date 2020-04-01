from rest_framework import serializers
from .models import Profile, Settings



class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Profile
        fields = ("__all__")
        depth = 1


class SettingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Settings
        fields = ("__all__")
        depth = 1