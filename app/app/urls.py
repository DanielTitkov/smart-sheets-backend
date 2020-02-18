from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/rest/accounts/', include('accounts.urls')),
    path('api/rest/', include("sheets.urls")),
]