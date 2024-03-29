# Generated by Django 4.0.5 on 2023-06-01 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mproduct', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DocAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('file', models.FileField(upload_to='uploads/', verbose_name='附件')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DocLibrary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('description', tinymce.models.HTMLField(blank=True, default='', null=True, verbose_name='描述')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_creator', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_operator', to=settings.AUTH_USER_MODEL, verbose_name='修改人')),
            ],
            options={
                'verbose_name': '文档库',
                'verbose_name_plural': '文档库',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DocCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('doc_library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_doc_library', to='mdoc.doclibrary', verbose_name='文档库')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_parent', to='mdoc.doccategory', verbose_name='父级对象')),
            ],
            options={
                'verbose_name': '分档分类',
                'verbose_name_plural': '分档分类',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('description', tinymce.models.HTMLField(blank=True, default='', null=True, verbose_name='描述')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
                ('type', models.CharField(choices=[('file', '文件'), ('link', '链接'), ('page', '网页')], default='page', max_length=20, verbose_name='项目类型')),
                ('content', tinymce.models.HTMLField(blank=True, null=True, verbose_name='文档正文')),
                ('link', models.URLField(blank=True, null=True, verbose_name='文档链接')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_creator', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('doc_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_doc_category', to='mdoc.doccategory', verbose_name='所属分类')),
                ('doc_library', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_doc_library', to='mdoc.doclibrary', verbose_name='所属文档库')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_operator', to=settings.AUTH_USER_MODEL, verbose_name='修改人')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_product', to='mproduct.product', verbose_name='所属产品')),
            ],
            options={
                'verbose_name': '文档',
                'verbose_name_plural': '文档',
                'ordering': ['id'],
            },
        ),
    ]
