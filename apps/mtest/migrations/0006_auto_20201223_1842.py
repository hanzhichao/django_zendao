# Generated by Django 2.0 on 2020-12-23 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mtest', '0005_auto_20201223_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('file', models.FileField(upload_to='uploads/', verbose_name='附件')),
                ('bug', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mtest_testattachment_test_case', to='mtest.Bug', verbose_name='Bug')),
                ('test_case', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mtest_testattachment_test_case', to='mtest.TestCase', verbose_name='测试用例')),
            ],
            options={
                'verbose_name': '附件',
                'verbose_name_plural': '附件',
                'ordering': ['id'],
            },
        ),
        migrations.RemoveField(
            model_name='attachment',
            name='bug',
        ),
        migrations.RemoveField(
            model_name='attachment',
            name='test_case',
        ),
        migrations.DeleteModel(
            name='Attachment',
        ),
    ]
