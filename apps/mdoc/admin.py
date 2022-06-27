from django.contrib import admin
from django import forms

from . import models

from utils.admin_utils import BaseAdmin, BaseTabularInline, BaseRecordAdmin, short_description


class DocCategoryChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.path


@admin.register(models.DocLibrary)
class DocLibraryAdmin(BaseAdmin):
    list_display = ('name', 'description', 'created', 'modified')

    class DocCategoryInline(BaseTabularInline):
        model = models.DocCategory

    inlines = [DocCategoryInline]


@admin.register(models.Doc)
class DocAdmin(BaseAdmin):
    list_display = ('name', 'type', 'creator', 'created', 'operations')
    list_filter = ('doc_library', 'doc_category')
    fields = (('project', 'product'), ('doc_library', 'doc_category'), 'type',
              'name', 'tags', 'link', 'content', 'description')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'doc_category':
            return DocCategoryChoiceField(label='所属分类', queryset=models.DocCategory.objects.all(), required=False)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

