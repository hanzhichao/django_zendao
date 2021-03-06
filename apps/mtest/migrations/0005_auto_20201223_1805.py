# Generated by Django 2.0 on 2020-12-23 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mproduct', '0003_auto_20201223_1805'),
        ('mtest', '0004_auto_20201223_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bug',
            name='related_version',
        ),
        migrations.RemoveField(
            model_name='testplan',
            name='related_version',
        ),
        migrations.AddField(
            model_name='bug',
            name='related_release',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mtest_bug_related_release', to='mproduct.ProductRelease', verbose_name='影响版本'),
        ),
        migrations.AddField(
            model_name='testplan',
            name='related_release',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mtest_testplan_related_version', to='mproduct.ProductRelease', verbose_name='关联版本'),
        ),
        migrations.AlterField(
            model_name='testplan',
            name='status',
            field=models.CharField(choices=[('new', '未开始'), ('processing', '进行中'), ('blocked', '被阻碍'), ('done', '完成')], default='new', max_length=20, verbose_name='当前状态'),
        ),
    ]
