# Generated by Django 2.0 on 2020-12-24 03:09

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mproject', '0009_auto_20201223_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', null=True, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', null=True, verbose_name='描述'),
        ),
    ]
