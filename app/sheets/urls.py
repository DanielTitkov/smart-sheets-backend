from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from .views import BlueprintView, DataView, SheetView

router = routers.DefaultRouter()
router.register(r'sheets', SheetView)
router.register(r'blueprints', BlueprintView)
router.register(r'datas', DataView)

urlpatterns = [
    path('', include(router.urls)),
]