# Generated by Django 4.0.5 on 2023-06-01 13:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('description', tinymce.models.HTMLField(blank=True, default='', null=True, verbose_name='描述')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
                ('key', models.CharField(max_length=200, unique=True, verbose_name='产品代号')),
                ('type', models.CharField(blank=True, choices=[('normal', '正常'), ('multi_branches', '多分支'), ('multi_platforms', '多平台')], max_length=20, null=True, verbose_name='产品类型')),
                ('view_control', models.CharField(choices=[('default', '默认'), ('private', '私有'), ('white_list', '白名单')], default='default', max_length=20, verbose_name='访问控制')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_creator', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_operator', to=settings.AUTH_USER_MODEL, verbose_name='修改人')),
                ('product_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_product_manager', to=settings.AUTH_USER_MODEL, verbose_name='产品负责人')),
                ('release_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_release_manager', to=settings.AUTH_USER_MODEL, verbose_name='发布负责人')),
                ('test_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_test_manager', to=settings.AUTH_USER_MODEL, verbose_name='测试负责人')),
            ],
            options={
                'verbose_name': '产品',
                'verbose_name_plural': '产品',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ProductRelease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='打包日期')),
                ('status', models.CharField(choices=[('ok', '正常'), ('停止维护', '停止维护')], default='ok', max_length=20, verbose_name='当前状态')),
            ],
            options={
                'verbose_name': '产品发布',
                'verbose_name_plural': '产品发布',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ProductVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('description', tinymce.models.HTMLField(blank=True, default='', null=True, verbose_name='描述')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
                ('build_date', models.DateField(blank=True, null=True, verbose_name='打包日期')),
                ('code_repo', models.CharField(blank=True, max_length=200, null=True, verbose_name='源代码地址')),
                ('download_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='下载地址')),
                ('builder', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_builder', to=settings.AUTH_USER_MODEL, verbose_name='构建者')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_creator', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_operator', to=settings.AUTH_USER_MODEL, verbose_name='修改人')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_product', to='mproduct.product', verbose_name='所属产品')),
            ],
            options={
                'verbose_name': '版本',
                'verbose_name_plural': '版本',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ReleasePackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('file', models.FileField(upload_to='uploads/', verbose_name='发行包')),
                ('product_release', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_product_release', to='mproduct.productrelease', verbose_name='所属发布')),
                ('product_version', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_product_version', to='mproduct.productversion', verbose_name='所属版本')),
            ],
            options={
                'verbose_name': '发行包',
                'verbose_name_plural': '发行包',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='productrelease',
            name='product_version',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_product_version', to='mproduct.productversion', verbose_name='所属版本'),
        ),
        migrations.CreateModel(
            name='ProductPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('start_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='开始日期')),
                ('end_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='结束日期')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_product', to='mproduct.product', verbose_name='所属产品')),
            ],
            options={
                'verbose_name': '发布计划',
                'verbose_name_plural': '发布计划',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ProductModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_parent', to='mproduct.productmodule', verbose_name='父级对象')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_product', to='mproduct.product', verbose_name='所属产品')),
            ],
            options={
                'verbose_name': '产品模块',
                'verbose_name_plural': '产品模块',
                'ordering': ['id'],
            },
        ),
    ]
