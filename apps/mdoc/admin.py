from django.contrib import admin
from django import forms

from . import models

from utils.admin_utils import BaseAdmin, BaseTabularInline, BaseRecordAdmin, short_description


class DocCategoryChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.path


@admin.register(models.DocLibrary)
class DocLibraryAdmin(BaseAdmin):
    admin_order = 1
    list_display = ('name', 'description', 'created', 'modified')

    class DocCategoryInline(BaseTabularInline):
        model = models.DocCategory

    inlines = [DocCategoryInline]


@admin.register(models.Doc)
class DocAdmin(BaseAdmin):
    admin_order = 2
    list_display = ('name', 'type', 'creator', 'created', 'operations')
    list_filter = ('doc_library', 'doc_category')
    # fields = (('project', 'product'), ('doc_library', 'doc_category'), 'type',
    #           'name', 'tags', 'link', 'content', 'description')

    fieldsets = [
        (
            None,
            {
                "fields": (('name', 'type',),
                           ('project', 'product'),
                           ('doc_library', 'doc_category'),
                           'description',
                           'content',)
            },
        ),
        (
            "其他",
            {
                "classes": ["collapse"],
                "fields": ['tags', 'link', ],
            },
        ),
    ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'doc_category':
            return DocCategoryChoiceField(label='所属分类', queryset=models.DocCategory.objects.all(), required=False)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)
