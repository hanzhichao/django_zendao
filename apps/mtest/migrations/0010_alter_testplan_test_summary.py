# Generated by Django 4.0.5 on 2022-06-28 03:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtest', '0009_alter_bug_assignee_alter_bug_cc_to_alter_bug_creator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testplan',
            name='test_summary',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='测试总结'),
        ),
    ]
