from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from .views import SheetList, BlueprintView, DataView

router = routers.DefaultRouter()
# router.register(r'sheets', SheetList, basename="sheet")
router.register(r'blueprints', BlueprintView)
router.register(r'datas', DataView)

urlpatterns = [
    path('', include(router.urls)),
    path('sheets/', SheetList.as_view()),
]