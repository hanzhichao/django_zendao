# Generated by Django 2.0 on 2020-12-23 03:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mproject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='mproject_project_manager', to=settings.AUTH_USER_MODEL, verbose_name='负责人'),
        ),
    ]
