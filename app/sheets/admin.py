from django.contrib import admin
from .models import Sheet, Data, Blueprint



class SheetAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'title',
        'type',
        'user', 
        'deleted',
        'created',
        'updated',
    )
    search_fields = (
        'title',
    )


class DataAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'sheet',
        'content',
        'created',
        'updated',
    )

class BlueprintAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'type',
        'desc',
    )


admin.site.register(Sheet, SheetAdmin)
admin.site.register(Data, DataAdmin)
admin.site.register(Blueprint, BlueprintAdmin)


