from django.contrib import admin
from django import forms

from . import models

from utils.admin_utils import BaseAdmin, BaseTabularInline, BaseRecordAdmin, short_description


@admin.register(models.Product)
class ProductAdmin(BaseAdmin):
    list_display = ('id', 'name', 'product_manager', 'test_manager', 'release_manager', 'requirements_num')

    class ProductBranchInline(BaseTabularInline):
        model = models.ProductBranch

    class ProductModuleInline(BaseTabularInline):
        model = models.ProductModule

    class ProductPlanInline(BaseTabularInline):
        model = models.ProductPlan

    @short_description('需求数量')
    def requirements_num(self, obj):
        return obj.mproduct_productrequirement_product.count()

    inlines = [ProductBranchInline, ProductModuleInline, ProductPlanInline]
    # fields = ('name', 'key', ('product_manager', 'test_manager', 'release_manager'), 'type', 'description', 'view_control')


@admin.register(models.ProductVersion)
class ProductVersionAdmin(BaseAdmin):
    class ProductReleaseInline(BaseTabularInline):
        model = models.ProductRelease

    class ReleasePackageInline(BaseTabularInline):
        model = models.ReleasePackage

    list_filter = ('product', 'builder')
    list_display = ('id', 'name', 'product', 'code_repo', 'download_url', 'build_date', 'builder', 'operations')
    inlines = [ProductReleaseInline, ReleasePackageInline]
    # fields = (('product', 'product_branch'), 'name',  ('builder', 'build_date'), 'code_repo', 'download_url', 'description')


class ProductPlanChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{} [{} ~ {}]".format(obj.name, obj.start_date, obj.end_date)


class ProductModuleChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.path


@admin.register(models.ProductRequirement)
class ProductRequirementAdmin(BaseAdmin):
    class ProductRequirementAttachmentInline(BaseTabularInline):
        model = models.ProductRequirementAttachment

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'product_plan':
            return ProductPlanChoiceField(label='所属计划', queryset=models.ProductPlan.objects.all(), required=False)

        if db_field.name == 'product_module':
            return ProductModuleChoiceField(label='所属模块', queryset=models.ProductModule.objects.all(), required=False)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = (
    'id', 'name', 'level', 'product_plan', 'source', 'assignee', 'estimated_time', 'status', 'stage', 'operations')
    list_filter = ('product_branch', 'product_module', 'status', 'stage', 'assignee', 'reviewer')
    search_fields = ('name',)
    inlines = [ProductRequirementAttachmentInline]
    readonly_fields = ('status',)
    # fields = (('product', 'product_branch', 'product_module'),
    #           ('product_plan', 'source'),
    #           ('reviewer', 'no_need_review'),
    #           ('name', 'level', 'estimated_time'),
    #           ('status', 'stage', 'assignee'),
    #           'description',
    #           'acceptance_criteria',
    #           'tags',
    #           'cc_to',
    #           )
    filter_horizontal = ('cc_to',)
