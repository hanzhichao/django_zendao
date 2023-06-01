from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.urls import path
from django.utils.safestring import mark_safe
from functools import wraps

# BASE_MODEL_ADMIN = admin.ModelAdmin
# BASE_TABULAR_INLINE = admin.TabularInline
# BASE_STACKED_INLINE = admin.StackedInline

import nested_admin
BASE_MODEL_ADMIN = nested_admin.NestedModelAdmin
BASE_TABULAR_INLINE = nested_admin.NestedTabularInline
BASE_STACKED_INLINE = nested_admin.NestedStackedInline
#
def short_description(text):
    def deco(func):
        @wraps(func)
        def new_func(*args, **kwargs):
            return func(*args, **kwargs)

        new_func.short_description = text
        return new_func
    return deco


class BaseRecordAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        self.readonly_fields = [field.name for field in self.model._meta.fields]

        return self.readonly_fields

    def has_add_permission(self, request):
        return False


class BaseAdmin(ImportExportModelAdmin, BASE_MODEL_ADMIN):
    list_display_links = ('name',)
    list_display = ('name',)
    exclude = ('creator', 'operator')
    extra_urls = []   # ('<pk>/run/', self.run)
    obj_operation_urls = []  # ('/run, '运行')
    obj_operation_sep = ' '

    def get_list_display(self, request):
        return self.list_display if 'id' in self.list_display else ['id', *self.list_display]


    def save_model(self, request, obj, form, change):
        if not obj.pk:  # 创建时
            obj.creator = request.user
        obj.operator = request.user
        super().save_model(request, obj, form, change)

    def get_urls(self):
        urls = super().get_urls()
        extra_urls = [path(*item) for item in self.extra_urls]
        return extra_urls + urls

    @short_description('操作')
    def operations(self, obj):
        tpl = '<a href="%s/{0}/">{1}</a>' % obj.pk
        operation_urls = [tpl.format(*item) for item in self.obj_operation_urls]
        link = self.obj_operation_sep.join(operation_urls)
        return mark_safe(link)

    @short_description('运行')
    def run(self, obj):
        if hasattr(obj, 'run'):
            getattr(obj, 'run')()

class BaseTabularInline(BASE_TABULAR_INLINE):
    extra = 0


class BaseStackedInline(BASE_STACKED_INLINE):
    extra = 0
