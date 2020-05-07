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
        'parent',
        'has_children',
        'published',
        'created',
        'updated',
    )
    search_fields = (
        'title',
    )
    list_filter = (
        'published',
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
    list_filter = (
        'deleted',
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

    def clean_rubric(self):
        rubric = self.cleaned_data['rubric']
        if rubric.has_children:
            raise forms.ValidationError('this rubric has children')
        return rubric



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

