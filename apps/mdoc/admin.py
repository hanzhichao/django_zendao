from django.contrib import admin

from . import models

from utils.admin_utils import BaseAdmin, BaseTabularInline, BaseRecordAdmin, short_description


@admin.register(models.DocLibrary)
class DocLibraryAdmin(BaseAdmin):
    list_display = ('name', 'description', 'created', 'modified')

    class DocCategoryInline(BaseTabularInline):
        model = models.DocCategory

    inlines = [DocCategoryInline]


@admin.register(models.Doc)
class DocAdmin(BaseAdmin):
    list_display = ('name', 'doc_category', 'description', 'created', 'modified')

