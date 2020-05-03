from django.contrib import admin
from django import forms

from django_admin_json_editor import JSONEditorWidget

from .models import Sheet, Data, Blueprint, Rubric
from .schemas import BLUEPRINT_SCHEMA


class RubricAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'title',
        'desc',
        'published',
        'created',
        'updated',
    )
    search_fields = (
        'title',
    )



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



class BlueprintAdminForm(forms.ModelForm):
    class Meta:
        model = Blueprint
        fields = '__all__'
        widgets = {
            'structure': JSONEditorWidget(BLUEPRINT_SCHEMA, collapsed=False, sceditor=True),
        }


admin.site.register(Sheet, SheetAdmin)
admin.site.register(Data, DataAdmin)
admin.site.register(Rubric, RubricAdmin)



@admin.register(Blueprint)
class BlueprintAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'type',
        'published',
        'desc',
    )
    form = BlueprintAdminForm

