# Generated by Django 2.0 on 2020-12-24 03:09

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mproduct', '0003_auto_20201223_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', null=True, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='productrequirement',
            name='description',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', null=True, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='productversion',
            name='description',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', null=True, verbose_name='描述'),
        ),
    ]