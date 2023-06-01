from django.contrib import admin
from django import forms
from django.contrib.auth.models import User

from utils.field_utils import UserChoiceField
from . import models

from utils.admin_utils import BaseAdmin, BaseTabularInline, BaseRecordAdmin, short_description


@admin.register(models.Project)
class ProjectAdmin(BaseAdmin):
    admin_order = 1
    list_display = ('name', 'key', 'project_manager', 'end_date', 'status', 'work_days')
    fields = ('name', 'key', ('start_date', 'end_date', 'work_days'), 'team_name',
              ('type', 'status'),
              ('project_manager', 'product_manager'),
              ('test_manager', 'release_manager'),
              'description', 'view_control')

    class ProjectRelatedProductInline(BaseTabularInline):
        model = models.ProjectRelatedProduct

    class ProjectMemberInline(BaseTabularInline):
        model = models.ProjectMember

    inlines = [ProjectRelatedProductInline, ProjectMemberInline]


class ProductPlanChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{} [{} ~ {}]".format(obj.name, obj.start_date, obj.end_date)


class ProductModuleChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.path


@admin.register(models.Requirement)
class RequirementAdmin(BaseAdmin):
    admin_order = 2

    class ProductRequirementAttachmentInline(BaseTabularInline):
        model = models.ProductRequirementAttachment

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'product_plan':
            return ProductPlanChoiceField(label='所属计划', queryset=models.ProductPlan.objects.all(), required=False)

        if db_field.name == 'product_module':
            return ProductModuleChoiceField(label='所属模块', queryset=models.ProductModule.objects.all(),
                                            required=False)

        if db_field.name == 'assignee':
            return UserChoiceField(label='指派给', queryset=User.objects.all(), required=False)

        if db_field.name == 'reviewer':
            return UserChoiceField(label='由谁评审', queryset=User.objects.all(), required=False)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = (
        'id', 'name', 'level', 'product_plan', 'source', 'assignee', 'estimated_time', 'status', 'stage', 'operations')
    list_filter = ('product_branch', 'product_module', 'status', 'stage', 'assignee', 'reviewer')
    search_fields = ('name',)
    inlines = [ProductRequirementAttachmentInline]
    readonly_fields = ('status',)
    fields = (('product', 'product_branch', 'product_module', 'product_plan',),
              ('name',  'source', 'level', 'estimated_time'),
              ('status', 'stage', 'assignee', 'reviewer', 'no_need_review'),
              'description',
              'acceptance_criteria',
              'tags',
              'cc_to',
              )
    filter_horizontal = ('cc_to',)


@admin.register(models.Task)
class TaskAdmin(BaseAdmin):
    admin_order = 3

    class TaskAttachmentInline(BaseTabularInline):
        model = models.TaskAttachment

    inlines = [TaskAttachmentInline]

    list_display = ('level', 'name', 'status', 'end_date', 'assignee')
    fields = (
        ('project', 'product_module'), 'name', ('assignee', 'level'), ('type', 'status'), ('start_date', 'end_date'),
        'description', 'cc_to')
    filter_horizontal = ('cc_to',)
