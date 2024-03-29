from pprint import pprint

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.urls import path
from django.utils.safestring import mark_safe
from functools import wraps

BASE_MODEL_ADMIN = admin.ModelAdmin
BASE_TABULAR_INLINE = admin.TabularInline
BASE_STACKED_INLINE = admin.StackedInline

# import nested_admin
# BASE_MODEL_ADMIN = nested_admin.NestedModelAdmin
# BASE_TABULAR_INLINE = nested_admin.NestedTabularInline
# BASE_STACKED_INLINE = nested_admin.NestedStackedInline
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

    actions = ['copy_objs']

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            try:
                if not instance.pk and instance.has_field('creator'):
                    instance.creator = request.user

                if  instance.has_field('operator'):
                    instance.operator = request.user
            except Exception:
                pass

            instance.save()
        formset.save_m2m()

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

    @admin.action(description='运行')
    def run(self, obj):
        if hasattr(obj, 'run'):
            getattr(obj, 'run')()

    @admin.display(description='优先级')
    def colored_priority(self, obj):
        colors_map = {
            'blocker': 'purple',
            'critical': 'red',
            'major': 'orange',
            'minor': 'blue',
            'trivial': 'grey',
        }
        color = colors_map.get(obj.priority, 'black')
        return mark_safe(
            '<span style="color: {};">{}</span>'.format(color, (obj.get_priority_display() or '-'))
        )

    @admin.action(description='复制')
    def copy_objs(self, request, queryset):
        for obj in queryset:
            obj.id = None
            obj.name = obj.name + '_复制'
            obj.save()

    def get_actions(self, request):
        actions = super().get_actions(request)
        # pprint(actions)
        # actions = list(actions) + ['copy_objs']
        # if 'copy_objs' not in actions:
            # actions['copy_objs'] = self.copy_objs
        # if 'delete_selected' in actions:
        #     del actions['delete_selected']
        return actions

class BaseTabularInline(BASE_TABULAR_INLINE):
    extra = 0


class BaseStackedInline(BASE_STACKED_INLINE):
    extra = 0
