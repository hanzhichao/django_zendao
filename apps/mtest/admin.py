from django.contrib import admin
from extra_settings.models import Setting

from msystem.admin import AttachmentInline
from . import models
from utils.admin_utils import BaseAdmin, BaseTabularInline, BaseRecordAdmin


@admin.register(models.TestCase)
class TestCaseAdmin(BaseAdmin):
    admin_order = 2
    list_display = ('name', 'level', 'product', 'type', 'creator', 'operations')
    list_editable = ('level', )
    list_filter = ('level', 'type', 'creator', 'product')


    class TestStepInline(BaseTabularInline):
        model = models.TestStep
        fields = ('order', 'name', 'excepted')

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
    list_display = ('name', 'manager', 'start_date', 'end_date', 'level', 'status', 'operations')
    # fields = ('project', 'related_release', 'manager', 'level', ('start_date', 'end_date'), 'status',
    #           'name', 'description', 'test_summary', 'cc_to')
    list_filter = ('related_release', 'project', 'level', 'status', 'manager')
    fieldsets = [
        (
            None,
            {
                "fields": (
                'name',
                ('project', 'related_release'),
                ('manager', 'level'),
                ('start_date', 'end_date'),
                'description',)
            },
        ),
        (
            "其他",
            {
                "classes": ["collapse"],
                "fields": ['status',
                    'test_summary', 'cc_to'],
            },
        ),
    ]

    class TestPlanCaseInline(BaseTabularInline):
        model = models.TestPlanCase

    inlines = [TestPlanCaseInline]
    filter_horizontal = ('cc_to',)
