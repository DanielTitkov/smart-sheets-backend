from django.contrib import admin
from .models import Profile, Settings



class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'user',
        'age',
        'sex',
        'city',
        'country',
        'created',
        'updated',
    )
    list_filter = (
        'sex',
        'city',
        'country',
    )



class SettingsAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'user',
        'encrypt',
        'created',
        'updated',
    )
    list_filter = (
        "encrypt",
    ) 



admin.site.register(Profile, ProfileAdmin)
admin.site.register(Settings, SettingsAdmin)