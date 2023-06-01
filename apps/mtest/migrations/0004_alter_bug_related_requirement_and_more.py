# Generated by Django 4.0.5 on 2023-06-01 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mproject', '0003_requirement_productrequirementattachment'),
        ('mtest', '0003_alter_testcase_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='related_requirement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related_requirement', to='mproject.requirement', verbose_name='关联需求'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='related_requirement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_related_requirement', to='mproject.requirement', verbose_name='关联需求'),
        ),
    ]