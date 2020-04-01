from django.urls import path, include
from rest_framework import routers
from .views import ProfileList, SettingsList

# urlpatterns = [
#     path('profile/', ProfileList.as_view())
# ]

router = routers.DefaultRouter()
# router.register(r'profiles', ProfileList.as_view(), basename="profile")
# router.register(r'settings', SettingsView,  basename="settings")

urlpatterns = [
    path('', include(router.urls)),
    path(r'profile', ProfileList.as_view()),
    path(r'settings', SettingsList.as_view()),
]