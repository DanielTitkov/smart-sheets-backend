from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from .views import BlueprintView, DataView, SheetView, RubricView

router = routers.DefaultRouter()
router.register(r'sheets', SheetView, basename="sheet")
router.register(r'blueprints', BlueprintView, basename="blueprint")
router.register(r'datas', DataView)
router.register(r'rubrics', RubricView, basename="rubric")

urlpatterns = [
    path('', include(router.urls)),
]