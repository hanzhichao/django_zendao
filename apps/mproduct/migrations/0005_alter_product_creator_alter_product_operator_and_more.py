# Generated by Django 4.0.5 on 2022-06-27 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mproduct', '0004_auto_20201224_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_creator', to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='product',
            name='operator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_operator', to=settings.AUTH_USER_MODEL, verbose_name='修改人'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_product_manager', to=settings.AUTH_USER_MODEL, verbose_name='产品负责人'),
        ),
        migrations.AlterField(
            model_name='product',
            name='release_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_release_manager', to=settings.AUTH_USER_MODEL, verbose_name='发布负责人'),
        ),
        migrations.AlterField(
            model_name='product',
            name='test_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_test_manager', to=settings.AUTH_USER_MODEL, verbose_name='测试负责人'),
        ),
        migrations.AlterField(
            model_name='productbranch',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_product', to='mproduct.product', verbose_name='所属产品'),
        ),
        migrations.AlterField(
            model_name='productmodule',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_parent', to='mproduct.productmodule', verbose_name='父级对象'),
        ),
        migrations.AlterField(
            model_name='productmodule',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_product', to='mproduct.product', verbose_name='所属产品'),
        ),
        migrations.AlterField(
            model_name='productmodule',
            name='product_branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_product_branch', to='mproduct.productbranch', verbose_name='所属分支'),
        ),
        migrations.AlterField(
            model_name='productplan',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_product', to='mproduct.product', verbose_name='所属产品'),
        ),
        migrations.AlterField(
            model_name='productplan',
            name='product_branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_product_branch', to='mproduct.productbranch', verbose_name='所属分支'),
        ),
        migrations.AlterField(
            model_name='productrelease',
            name='product_version',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_product_version', to='mproduct.productversion', verbose_name='所属版本'),
        ),
        migrations.AlterField(
            model_name='productrequirement',
            name='assignee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_assignee', to=settings.AUTH_USER_MODEL, verbose_name='指派给'),
        ),
        migrations.AlterField(
            model_name='productrequirement',
            name='cc_to',
            field=models.ManyToManyField(blank=True, related_name='%(app_label)s_%(class)s_cc_to', to=settings.AUTH_USER_MODEL, verbose_name='抄送给'),
        ),
        migrations.AlterField(
            model_name='productrequirement',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_creator', to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='productrequirement',
            name='operator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_operator', to=settings.AUTH_USER_MODEL, verbose_name='修改人'),
        ),
        migrations.AlterField(
            model_name='productrequirement',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_product', to='mproduct.product', verbose_name='所属产品'),
        ),
        migrations.AlterField(
            model_name='productrequirement',
            name='product_branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_product_branch', to='mproduct.productbranch', verbose_name='所属分支'),
        ),
        migrations.AlterField(
            model_name='productrequirement',
            name='product_module',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_module', to='mproduct.productmodule', verbose_name='所属模块'),
        ),
        migrations.AlterField(
            model_name='productrequirement',
            name='product_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_plan', to='mproduct.productplan', verbose_name='所属计划'),
        ),
        migrations.AlterField(
            model_name='productrequirement',
            name='reviewer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_reviewer', to=settings.AUTH_USER_MODEL, verbose_name='由谁评审'),
        ),
        migrations.AlterField(
            model_name='productrequirementattachment',
            name='product_requirement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_product_requirement', to='mproduct.productrequirement', verbose_name='所属需求'),
        ),
        migrations.AlterField(
            model_name='productversion',
            name='builder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_builder', to=settings.AUTH_USER_MODEL, verbose_name='构建者'),
        ),
        migrations.AlterField(
            model_name='productversion',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_creator', to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='productversion',
            name='operator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_operator', to=settings.AUTH_USER_MODEL, verbose_name='修改人'),
        ),
        migrations.AlterField(
            model_name='productversion',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_product', to='mproduct.product', verbose_name='所属产品'),
        ),
        migrations.AlterField(
            model_name='productversion',
            name='product_branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_product_branch', to='mproduct.productbranch', verbose_name='所属分支'),
        ),
        migrations.AlterField(
            model_name='releasepackage',
            name='product_release',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_product_release', to='mproduct.productrelease', verbose_name='所属发布'),
        ),
        migrations.AlterField(
            model_name='releasepackage',
            name='product_version',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_product_version', to='mproduct.productversion', verbose_name='所属版本'),
        ),
    ]
