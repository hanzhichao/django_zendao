# Generated by Django 2.0 on 2020-12-23 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mproject', '0007_auto_20201223_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='task_project', to='mproject.Project', verbose_name='所属项目'),
            preserve_default=False,
        ),
    ]
