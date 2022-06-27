# Generated by Django 4.0.5 on 2022-06-27 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mproduct', '0005_alter_product_creator_alter_product_operator_and_more'),
        ('mproject', '0011_alter_project_creator_alter_project_members_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mtest', '0008_auto_20201224_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='assignee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_assignee', to=settings.AUTH_USER_MODEL, verbose_name='指派给'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='cc_to',
            field=models.ManyToManyField(blank=True, related_name='%(app_label)s_%(class)s_cc_to', to=settings.AUTH_USER_MODEL, verbose_name='抄送给'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_creator', to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='operator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_operator', to=settings.AUTH_USER_MODEL, verbose_name='修改人'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_product', to='mproduct.product', verbose_name='所属产品'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='product_branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_product_branch', to='mproduct.productbranch', verbose_name='所属分支'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='product_module',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_module', to='mproduct.productmodule', verbose_name='所属模块'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_project', to='mproject.project', verbose_name='所属项目'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='related_release',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related_release', to='mproduct.productrelease', verbose_name='影响版本'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='related_requirement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related_requirement', to='mproduct.productrequirement', verbose_name='关联需求'),
        ),
        migrations.AlterField(
            model_name='bug',
            name='related_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related_requirement', to='mproject.task', verbose_name='关联任务'),
        ),
        migrations.AlterField(
            model_name='testattachment',
            name='bug',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_test_case', to='mtest.bug', verbose_name='Bug'),
        ),
        migrations.AlterField(
            model_name='testattachment',
            name='test_case',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_test_case', to='mtest.testcase', verbose_name='测试用例'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_creator', to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='operator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_operator', to=settings.AUTH_USER_MODEL, verbose_name='修改人'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_product', to='mproduct.product', verbose_name='所属产品'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='product_branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_product_branch', to='mproduct.productbranch', verbose_name='所属分支'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='product_module',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_module', to='mproduct.productmodule', verbose_name='所属模块'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='related_requirement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related_requirement', to='mproduct.productrequirement', verbose_name='关联需求'),
        ),
        migrations.AlterField(
            model_name='testcaserecord',
            name='test_case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_test_case', to='mtest.testcase', verbose_name='测试用例'),
        ),
        migrations.AlterField(
            model_name='testplan',
            name='cc_to',
            field=models.ManyToManyField(blank=True, related_name='%(app_label)s_%(class)s_cc_to', to=settings.AUTH_USER_MODEL, verbose_name='抄送给'),
        ),
        migrations.AlterField(
            model_name='testplan',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_creator', to=settings.AUTH_USER_MODEL, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='testplan',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_manager', to=settings.AUTH_USER_MODEL, verbose_name='负责人'),
        ),
        migrations.AlterField(
            model_name='testplan',
            name='operator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_operator', to=settings.AUTH_USER_MODEL, verbose_name='修改人'),
        ),
        migrations.AlterField(
            model_name='testplan',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_project', to='mproject.project', verbose_name='所属项目'),
        ),
        migrations.AlterField(
            model_name='testplan',
            name='related_release',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related_version', to='mproduct.productrelease', verbose_name='关联版本'),
        ),
        migrations.AlterField(
            model_name='testplancase',
            name='test_case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_test_case', to='mtest.testcase', verbose_name='测试用例'),
        ),
        migrations.AlterField(
            model_name='testplancase',
            name='test_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_test_case', to='mtest.testplan', verbose_name='测试计划'),
        ),
        migrations.AlterField(
            model_name='testplancase',
            name='tester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_operator', to=settings.AUTH_USER_MODEL, verbose_name='执行人'),
        ),
        migrations.AlterField(
            model_name='teststep',
            name='test_case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_test_case', to='mtest.testcase', verbose_name='测试用例'),
        ),
    ]