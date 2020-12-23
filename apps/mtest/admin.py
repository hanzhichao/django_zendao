from django.contrib import admin

from . import models
from utils.admin_utils import BaseAdmin, BaseTabularInline, BaseRecordAdmin, short_description


@admin.register(models.TestPlan)
class TestPlanAdmin(BaseAdmin):
    list_display = ('name', 'created', 'modified')

    class TestPlanCaseInline(BaseTabularInline):
        model = models.TestPlanCase

    inlines = [TestPlanCaseInline]


@admin.register(models.TestCase)
class TestCaseAdmin(BaseAdmin):
    list_display = ('name', 'stage', 'level', 'stage', 'tags', 'created', 'modified')

    class TestStepInline(BaseTabularInline):
        model = models.TestStep
        exclude = ('test_project',)

    inlines = [TestStepInline]


# @admin.register(models.TestReport)
# class TestReportAdmin(BaseRecordAdmin):
#     list_display = ('created', 'test_plan', 'status')
#     list_display_links = ('created', )
#
#     class TestCaseRecordInline(BaseTabularInline):
#         model = models.TestCaseRecord
#
#         def has_add_permission(self, request):
#             return False
#
#     inlines = [TestCaseRecordInline]