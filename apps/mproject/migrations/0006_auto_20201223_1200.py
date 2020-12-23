# Generated by Django 2.0 on 2020-12-23 04:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mproject', '0005_auto_20201223_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='manager',
        ),
        migrations.AddField(
            model_name='project',
            name='project_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='mproject_project_manager', to=settings.AUTH_USER_MODEL, verbose_name='项目负责人'),
        ),
        migrations.AlterField(
            model_name='project',
            name='stage',
            field=models.CharField(blank=True, choices=[('new', '未开始'), ('processing', '进行中'), ('hang_up', '已挂起'), ('done', '已完成')], default='new', max_length=20, null=True, verbose_name='项目状态'),
        ),
    ]