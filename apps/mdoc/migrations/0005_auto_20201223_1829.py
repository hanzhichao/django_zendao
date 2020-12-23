# Generated by Django 2.0 on 2020-12-23 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mdoc', '0004_remove_doc_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='doc_library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mdoc_doc_doc_library', to='mdoc.DocLibrary', verbose_name='所属文档库'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mdoc_doc_product', to='mproduct.Product', verbose_name='所属产品'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mdoc_doc_project', to='mproject.Project', verbose_name='所属项目'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='type',
            field=models.CharField(choices=[('file', '文件'), ('link', '链接'), ('page', '网页')], default='page', max_length=20, verbose_name='项目类型'),
        ),
    ]