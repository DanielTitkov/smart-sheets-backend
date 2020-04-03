from rest_framework import viewsets
from django.conf import settings
from .models import Profile, Settings
from .serializers import ProfileSerializer, SettingSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SettingsList(APIView):

    def get(self, request, format=None):
        user = self.request.user
        user_settings = Settings.objects.filter(user=user).first()
        if not user_settings:
            user_settings = Settings.objects.create(user=user, **settings.USER_DEFAULT_SETTINGS) # create with default values if not exist
        serializer = SettingSerializer(user_settings)
        return Response(serializer.data)

    def post(self, request, format=None):
        user = self.request.user
        serializer = SettingSerializer(data=request.data, context={'request': self.request})
        if serializer.is_valid(): 
            serializer.instance = Settings.objects.filter(user=user).first()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProfileList(APIView):

    def get(self, request, format=None):
        user = self.request.user
        profile = Profile.objects.filter(user=user).first()
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


    def post(self, request, format=None):
        user = self.request.user
        serializer = ProfileSerializer(data=request.data, context={'request': self.request})
        if serializer.is_valid(): 
            profile = Profile.objects.filter(user=user).first()
            if profile: # if profile exists - udpate, else create new
                if not Profile.is_new_data(profile, serializer.validated_data): 
                    # check if profile is really updated? If not, just return 
                    return Response(serializer.data, status=status.HTTP_200_OK)
                serializer.instance = profile # not sure if this is safe
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)