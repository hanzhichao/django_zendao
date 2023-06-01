from django.contrib import admin

from . import models
from utils.admin_utils import BaseAdmin, BaseTabularInline, BaseRecordAdmin, short_description


@admin.register(models.Bug)
class BugAdmin(BaseAdmin):
    admin_order = 1
    list_display = ('name', 'level', 'severity', 'status', 'creator', 'assignee')

    class TestAttachmentInline(BaseTabularInline):
        model = models.TestAttachment
        exclude = ('test_case',)

    inlines = [TestAttachmentInline]

    fields = (('product', 'product_branch', 'product_module'),
              ('project', 'related_release'),
              'assignee',
              ('type', 'platform', 'browser'),
              ('name', 'severity', 'level'),
              ('related_requirement', 'related_task'),
              'tags',
              'cc_to'
              )
    filter_horizontal = ('cc_to',)


@admin.register(models.TestCase)
class TestCaseAdmin(BaseAdmin):
    admin_order = 2
    list_display = ('level', 'product_branch', 'name', 'type', 'creator', 'operations')

    class TestStepInline(BaseTabularInline):
        model = models.TestStep

    class TestAttachmentInline(BaseTabularInline):
        model = models.TestAttachment
        exclude = ('bug',)

    inlines = [TestStepInline, TestAttachmentInline]
    fields = (('product', 'product_branch', 'product_module'),
              ('type', 'stage'),
              'related_requirement',
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
    filter_horizontal = ('cc_to',)
