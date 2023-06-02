from django.contrib import admin
from extra_settings.models import Setting

from msystem.admin import AttachmentInline
from . import models
from utils.admin_utils import BaseAdmin, BaseTabularInline, BaseRecordAdmin


@admin.register(models.Bug)
class BugAdmin(BaseAdmin):
    admin_order = 1
    list_display = ('id', 'name', 'level', 'severity', 'status', 'creator', 'assignee')
    list_display_links = ('name',)
    list_filter = ('level', 'severity', 'status', 'creator', 'assignee')


    inlines = [AttachmentInline]

    fields = (('product', 'product_module', 'project', 'related_release'),
              ('name', 'severity', 'level', 'assignee'),
              ('type', 'platform', 'browser'),
              ('related_requirement', 'related_task'),
              'tags',
              'description',
              'cc_to'
              )
    filter_horizontal = ('cc_to',)

    def formfield_for_choice_field(self, db_field, request, **kwargs):

        if db_field.name == "severity":
            value = Setting.get("BUG_SEVERITY")
            if value:
                choices = list(zip(range(len(value)), value))
            kwargs['choices'] = choices
            # if request.user.is_superuser:
            #     kwargs['choices'] += (('ready', 'Ready for deployment'),)
        return super().formfield_for_choice_field(db_field, request, **kwargs)


@admin.register(models.TestCase)
class TestCaseAdmin(BaseAdmin):
    admin_order = 2
    list_display = ('name', 'level', 'product',  'type', 'creator', 'operations')

    class TestStepInline(BaseTabularInline):
        model = models.TestStep

    inlines = [TestStepInline, AttachmentInline]
    fields = (('product', 'product_module'),
              ('type', 'stage', 'related_requirement'),
              ('name', 'level'),
              'pre_condition',
              'tags',
              )


@admin.register(models.TestPlan)
class TestPlanAdmin(BaseAdmin):
    admin_order = 3
    list_display = ('name', 'manager', 'start_date', 'end_date', 'status', 'operations')
    fields = ('project', 'related_release', 'manager', 'level', ('start_date', 'end_date'), 'status',
              'name', 'description', 'test_summary', 'cc_to')

    class TestPlanCaseInline(BaseTabularInline):
        model = models.TestPlanCase

    inlines = [TestPlanCaseInline]
    filter_horizontal = ('cc_to', )
