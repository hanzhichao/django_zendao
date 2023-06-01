from django.contrib import admin
from django import forms
from django.contrib.auth.models import User

from utils.field_utils import UserChoiceField
from . import models

from utils.admin_utils import BaseAdmin, BaseTabularInline, BaseRecordAdmin, short_description


@admin.register(models.Product)
class ProductAdmin(BaseAdmin):
    admin_order = 1
    list_display = ('id', 'name', 'product_manager', 'test_manager', 'release_manager', 'requirements_num')

    # class ProductBranchInline(BaseTabularInline):
    #     model = models.ProductBranch

    class ProductModuleInline(BaseTabularInline):
        model = models.ProductModule

    # class ProductPlanInline(BaseTabularInline):
    #     model = models.ProductPlan

    # inlines = [ProductModuleInline, ProductPlanInline]
    @short_description('需求数量')
    def requirements_num(self, obj):
        return obj.mproject_requirement_product.count()

    inlines = [ProductModuleInline]
    fields = (
        'name', 'key', ('product_manager', 'test_manager', 'release_manager'), 'type', 'description', 'view_control')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if db_field.name == 'product_manager':
            return UserChoiceField(label='产品负责人', queryset=User.objects.all(), required=False)

        if db_field.name == 'test_manager':
            return UserChoiceField(label='测试负责人', queryset=User.objects.all(), required=False)

        if db_field.name == 'release_manager':
            return UserChoiceField(label='发布负责人', queryset=User.objects.all(), required=False)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(models.ProductVersion)
class ProductVersionAdmin(BaseAdmin):
    admin_order = 2

    class ProductReleaseInline(BaseTabularInline):
        class ReleasePackageInline(BaseTabularInline):
            model = models.ReleasePackage

        model = models.ProductRelease
        inlines = [ReleasePackageInline]

    list_filter = ('product', 'builder')
    list_display = ('id', 'name', 'product', 'code_repo', 'download_url', 'build_date', 'builder', 'operations')
    inlines = [ProductReleaseInline]
    fields = ('name', 'product',  ('builder', 'build_date'), ('code_repo', 'download_url'), 'description')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'builder':
            return UserChoiceField(label='构建者', queryset=User.objects.all(), required=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(models.ProductPlan)
class ProductPlanAdmin(BaseAdmin):
    admin_order = 3
    list_display = ('id', 'name', 'product', 'start_date', 'end_date')
    list_filter = ('product',)
